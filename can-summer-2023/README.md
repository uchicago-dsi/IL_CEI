## Opportunity to Grow: Minority Participation in Government Bids and Contracts in Illinois
### CAN Summer Experience (2023)

#### Background
The State of Illinois purchases billions of dollars in goods, services, and works (construction) from the private sector each year in a process known as _public procurement_. These purchases include everything that its departments and agencies need to function, from small items like food and office furniture to buses, asphalt equipment, software licenses, contractors, and consulting services. However, businesses owned by racial minorities, women, and persons with disabilities are often underrepresented among the government’s vendors—a social justice issue with negative economic impacts given that contracts can lead to job creation and increased tax revenue for the communities in which the vendors are located.

To address this problem, the state has created the Business Enterprise Program (BEP), which promotes fair and equitable public contracting opportunities for these groups. The Illinois Committee on Equity and Inclusion (CEI) now manages the program and would like to better promote it, as the BEP budget has not been fully utilized for the last 10 years. This project will move CEI towards its goal by raising public awareness of procurement disparities. The repository contains a geospatial analysis of state-level procurement data, mapping patterns of companies, bids, and awarded contracts by BEP certification status and investigating which areas are receiving the benefits of those contracts.

#### Directory

**data**: Contains datasets used in the analysis.

- cache: Stores the results of forward geocoding using the Bing Maps API.

- clean: Directory containing cleaned datasets for BEP company addresses, locations, and census tract demographics. Created from the raw datasets.

- raw: Directory containing data on BEP-certified companies as well as state vendors, bids, and contracts downloaded from the state's e-procurement system, BidBuy. Also contains census tract boundaries for the state merged with population, education, and income demographics exported from Social Explorer.


**notebooks**: Contains Jupyter notebooks used for the analysis.

- clean_bep_companies.ipynb: Cleans and/or geocodes companies' addresses and BEP certifications. To run, requires a `.env` file containing an environment variable called `BING_API_KEY`.

- clean_tracts.ipynb: Creates datasets of demographic data (e.g., population, education, and income) for census tracts across the state.

