cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
library(ggplot2)

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/plots_moz/MOZILLA.csv"
# THE_LIMIT   <- 77
# THE_DS_NAME <- "MOZILLA"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/plots_ost/OPENSTACK.csv"
# THE_LIMIT   <- 100
# THE_DS_NAME <- "OPENSTACK"

# THE_FILE   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/plots_wik/WIKIMEDIA.csv"
# THE_LIMIT  <- 105
# THE_DS_NAME <- "WIKIMEDIA"

# Y_LABEL     <- "Count of Smells per File"
# Y_LABEL     <- "Smell Density (KLOC)"
Y_LABEL     <- "Script (%)"

#SMELL_DENSITY  ,  CNT_PER_FIL , UNI_FIL_PER

LINE_DATA <- read.csv(THE_FILE)
the_plot  <- ggplot(data=LINE_DATA, aes(x=MONTH, y=UNI_FIL_PER, group=1)) + 
  geom_point(size=0.1) + scale_x_discrete(breaks = LINE_DATA$MONTH[seq(1, length(LINE_DATA$MONTH), by = THE_LIMIT)]) + 
  geom_smooth(size=0.95, aes(color=TYPE), method='loess') +   
  facet_grid( . ~ TYPE) +
  labs(x='Month', y=Y_LABEL) +
  theme(legend.position="none") +
  ggtitle(THE_DS_NAME) + theme(plot.title = element_text(hjust = 0.5)) +
  theme(text = element_text(size=11), axis.text.x = element_text(angle=45, hjust=1, size=11), axis.text.y = element_text(size=11), axis.title=element_text(size=11, face="bold"))  

the_plot <- the_plot + facet_wrap(~ TYPE, ncol=4)
the_plot

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))