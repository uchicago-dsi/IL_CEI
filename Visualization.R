require(ggplot2)
require(dplyr)
require(tidyr)
require(superheat)
require(tibble)
require(gghighlight)

#install.packages("Rcpp", dependencies = TRUE, INSTALL_opts = '--no-lock').
#install.packages("lifest", dependencies = TRUE, INSTALL_opts = '--no-lock').

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






# Plot 2
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

