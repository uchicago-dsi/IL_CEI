require(ggplot2)
require(dplyr)
require(tidyr)
require(superheat)
require(tibble)
require(gghighlight)

#install.packages("Rcpp", dependencies = TRUE, INSTALL_opts = '--no-lock').
#install.packages("lifest", dependencies = TRUE, INSTALL_opts = '--no-lock').

#### Data Cleaning and Heatmap #####

data = read.csv("Dashboard_Raw_Data.csv")

# create year column and trim the dataset
data$year = as.integer(substr(data$FISCAL.YEARS, 4, 7))
data = data[!is.na(data$year),]

# clean columns
data$DOLLARS.ACHIEVED = as.integer(data$DOLLARS.ACHIEVED)
data$X20..GOAL = as.integer(data$X20..GOAL)

# plots (and data cleaned specifically for plots)
pdat = data %>% 
  mutate(ratio = DOLLARS.ACHIEVED/X20..GOAL) %>% 
  select(NAME, year, ratio) %>%
  pivot_wider(names_from = year, values_from = ratio) %>%
  column_to_rownames(var = "NAME")

#pdat_No_NA = pdat[!rowSums(is.na(pdat[colnames(pdat)])),]
pdat_No_NA = pdat %>% 
  mutate(
    across(
      everything(), 
      function(.x) .x <- ifelse(is.na(.x), -999, .x)
    )
  )
rownames(pdat_No_NA) = rownames(pdat) 
  
heatmap = superheat(
  pdat_No_NA,
  legend = FALSE,
  force.left.label = TRUE,
  left.label.text.size = 5, 
  left.label.size = 0.3,
  bottom.label.text.size = 15,
  bottom.label.size = 0.083,
  bottom.label.text.alignment = "right",
  pretty.order.rows = TRUE, 
  row.dendrogram = FALSE,
  heat.pal = c('#0F4D92','#00CCFF','#ADD8E6','#FFFFFF','#FFFFFF'),
  heat.pal.values = c(0, 0.5/260, 0.99999999/260, 1/260, 1),
  heat.lim = c(0, 260), 
  bottom.label.text.angle = 80,
  bottom.label.col = "#b3e2cd",
#  legend.breaks = c(0,1, 260),
 # legend.width = 20,
 # legend.height = 0.23,
#  legend.text.size = 15,
  grid.hline = FALSE,
  print.plot = FALSE
)
x = heatmap$plot
legends = ggplot(data.frame(x = c(0,0.5,0.999)), aes(x, x, fill = x)) + 
  scale_fill_gradient2(low = '#0F4D92',
                        midpoint = 0.5,
                        mid = '#00CCFF',
                        high = '#ADD8E6',
                        space="Lab")+ 
  geom_point() +
  theme(legend.position = "bottom", legend.title=element_blank()) + 
  theme(legend.key.size = unit(2, 'cm'), legend.key.width= unit(4, 'cm'),
        legend.text = element_text(size=15))
         
legends = ggpubr::get_legend(legends)
#legends = ggpubr::as_ggplot(legends)

#plot_W_legend = ggpubr::ggarrange(heatmap, ncol = 1, nrow = 1, legend.grob = legends)

plot_W_legend <- cowplot::plot_grid(heatmap$plot, legends,
                                    ncol = 1, nrow = 2,
                                    rel_heights = c(20, 2))

ggsave(plot = plot_W_legend, file = "heatMap.jpg",
       width = 100, height = 100, 
       units = "cm", dpi = 300)




#max(pdat$`2021`[!is.na(pdat$`2021`)])


######## End of Section ###############



###### Plot 2: Data Cleaning & Faceted Line Charts ########


pdat_long = pdat %>% 
  mutate(Facet = ifelse(apply(pdat > 10, 1, function(j) any(j, na.rm = TRUE)), ">10", "Others")) %>%
  rownames_to_column(var = "Agency") %>% 
  pivot_longer(cols = starts_with("20"),
               names_to = "Year",
               values_to = "Attainment Ratio",
               values_drop_na = TRUE
               ) %>%
  mutate(Year = as.numeric(Year))



x = ggplot(pdat_long[pdat_long$Facet == ">10",], aes(x = Year, y = `Attainment Ratio`, color = Agency)) + 
  geom_line(alpha = 0.5) +
  theme_minimal() + 
  theme(legend.position="none") +
  scale_x_continuous(breaks = 2013:2021, labels = as.character(2013:2021))+
  gghighlight(max(`Attainment Ratio`) > 100, line_label_type = "ggrepel_text")+
  facet_grid(Facet ~ .)
  

y = ggplot(pdat_long[pdat_long$Facet == "Others",], aes(x = Year, y = `Attainment Ratio`, color = Agency)) + 
  geom_line(alpha = 0.5) +
  theme_minimal() + 
  theme(legend.position="none") +
  scale_x_continuous(breaks = 2013:2021, labels = as.character(2013:2021)) + facet_grid(Facet ~ .)

z = ggpubr::ggarrange(x, y, ncol = 1, nrow = 2)

ggsave(plot = z, file = "Facet_Line.jpg",
       width = 20, height = 20, 
       units = "cm", dpi = 300)
ggsave(plot = x, file = "Facet_Line_Highlights.jpg",
       width = 30, height = 20, 
       units = "cm", dpi = 300)

########## End of Section ##############




#### Plots 3: Data Cleaninig and By-county (zipcode) visualization

data = read.csv("full_zipcode.csv") 
# This file contains only 4 columns of the cleaned (no duplicates) certification data
# The columns are: Company Namem,	Ethnicity,	Gender,	County
data$County = toupper(data$County)
type = levels(factor(data$Ethnicity))
type

dat_AA = data[which(data$Ethnicity == "African American"),]
dat_ASA = data[which(data$Ethnicity=="Asian American"),]
dat_HA = data[which(data$Ethnicity=="Hispanic" | data$Ethnicity=="Hispanic/Latino"),]
dat_NA = data[which(data$Ethnicity=="Native American"),]
dat_F = data[which(data$Gender == "Female"),]

data_total = data[which(data$Gender == "Female" | 
                          data$Ethnicity == "African American" |
                          data$Ethnicity == "Asian American"| 
                          data$Ethnicity=="Hispanic" | data$Ethnicity=="Hispanic/Latino"|
                          data$Ethnicity=="Native American"),]
dat = list(dat_AA, dat_ASA, dat_HA, dat_NA, dat_F, data_total)

require(maps)
require(ggmap)
require(mapdata)

states = map_data("state")
IL = subset(states, region %in% c("illinois"))
counties = map_data("county")
IL_county = subset(counties, region == "illinois")
IL_county$County = toupper(IL_county$subregion)

il_base = ggplot(data = IL, mapping = aes(x = long, y = lat, group = group)) + 
  coord_fixed(1.3) + 
  geom_polygon(color = "black", fill = NA) + 
  theme_nothing() 

names = c("African American", "Asian American", "HispanicLatino", "Native American", "Female","All")

for (i in 1:6){
  t = dat[[i]]
  t = t %>% group_by(County) %>% summarise(n = n())
  x = IL_county %>% left_join(t)
  
  il_plot = il_base + geom_polygon(data = x, color = "black", aes(fill = n)) +
    theme(legend.position = "right")
  
  ggsave(plot = il_plot, file = paste0("byCounty_",names[i],".jpg"),
         width = 30, height = 20, 
         units = "cm", dpi = 300)
}


######### End of Section #########


################## Subsection: Plot by Zipcode ###############
require(usa)
zcs = usa::zipcodes %>% subset(state == "IL")

for (i in 1:6){
  x = dat[[i]]  %>% mutate(zip = stringr::str_trim(as.character(Zip)))
  y = x %>% left_join(zcs)
  
  il_plot = ggplot(data = IL, mapping = aes(x = long, y = lat)) + 
    coord_fixed(1.3) + 
    geom_polygon(color = "black", fill = NA, aes(group = group)) + 
    theme_nothing()  + 
    geom_polygon(data = IL_county, fill = NA, color = "black", aes(group = group)) +
    geom_point(data = y, color = "blue", alpha = 0.1) +
    theme(legend.position = "right") 
  
  ggsave(plot = il_plot, file = paste0("byZipCode_",names[i],".jpg"),
         width = 30, height = 20, 
         units = "cm", dpi = 300)
}
