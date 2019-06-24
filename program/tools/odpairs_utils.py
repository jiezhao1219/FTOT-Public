# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 11:09:51 2018

@author: Matthew.Pearlson.CTR
"""

import csv
import sys
import os
import glob
import ntpath
    


log_dir = os.curdir 
print log_dir

#make a directory for the report to go into
report_directory = os.path.join(log_dir, "report")
if not os.path.exists(report_directory):
    os.makedirs(report_directory)

report_file_name = "report_od_pairs.csv"
report_file = os.path.join(report_directory, report_file_name)

    
# get all of the csv files matching the pattern
 
log_files = glob.glob(os.path.join(log_dir, "*.csv"))
print  "len(log_files): {}".format(len(log_files))                                                    

from_location_list = []
to_location_list = []
location_list = [] 
# add log file name and date to dictionary.  each entry in the array
# will be a tuple of (log_file_name, datetime object)

# out locations that are showing up uniquely
out_string = "99_OUT,98_OUT,97_OUT,96_OUT,95_OUT,94_OUT,93_OUT,92_OUT,91_OUT,90_OUT,9_OUT,89_OUT,88_OUT,87_OUT,86_OUT,85_OUT,84_OUT,83_OUT,82_OUT,81_OUT,80_OUT,8_OUT,79_OUT,78_OUT,77_OUT,76_OUT,75_OUT,74_OUT,73_OUT,72_OUT,71_OUT,70_OUT,7_OUT,69_OUT,68_OUT,67_OUT,66_OUT,65_OUT,64_OUT,63_OUT,62_OUT,61_OUT,60_OUT,6_OUT,59_OUT,58_OUT,57_OUT,56_OUT,55_OUT,54_OUT,53_OUT,52_OUT,51_OUT,50_OUT,5_OUT,49_OUT,48_OUT,47_OUT,46_OUT,45_OUT,44_OUT,43_OUT,42_OUT,41_OUT,40_OUT,4_OUT,39_OUT,38_OUT,37_OUT,36_OUT,35_OUT,34_OUT,33_OUT,32_OUT,31_OUT,3056_OUT,3023_OUT,30_OUT,3_OUT,2957_OUT,2956_OUT,2955_OUT,2954_OUT,2950_OUT,2949_OUT,2938_OUT,2937_OUT,2936_OUT,2935_OUT,2934_OUT,2933_OUT,2932_OUT,2910_OUT,2909_OUT,2908_OUT,2907_OUT,2906_OUT,2905_OUT,2904_OUT,2902_OUT,2901_OUT,2900_OUT,29_OUT,2899_OUT,2898_OUT,2891_OUT,2890_OUT,2889_OUT,2888_OUT,2870_OUT,2869_OUT,2868_OUT,2867_OUT,2865_OUT,2864_OUT,2848_OUT,2847_OUT,2846_OUT,2845_OUT,2844_OUT,2843_OUT,2842_OUT,2841_OUT,2840_OUT,2839_OUT,2838_OUT,2837_OUT,2836_OUT,2835_OUT,2834_OUT,2833_OUT,2832_OUT,2831_OUT,2830_OUT,2829_OUT,2828_OUT,2827_OUT,2826_OUT,2825_OUT,2824_OUT,2823_OUT,2822_OUT,2821_OUT,2820_OUT,2819_OUT,2818_OUT,2817_OUT,2816_OUT,2815_OUT,2814_OUT,2813_OUT,2812_OUT,2811_OUT,2810_OUT,2809_OUT,2808_OUT,2807_OUT,2806_OUT,2805_OUT,2804_OUT,2803_OUT,2802_OUT,2801_OUT,2800_OUT,28_OUT,2799_OUT,2798_OUT,2797_OUT,2796_OUT,2795_OUT,2794_OUT,2793_OUT,2792_OUT,2791_OUT,2790_OUT,2789_OUT,2788_OUT,2787_OUT,2786_OUT,2785_OUT,2784_OUT,2783_OUT,2782_OUT,2781_OUT,2780_OUT,2779_OUT,2778_OUT,2777_OUT,2776_OUT,2775_OUT,2774_OUT,2773_OUT,2772_OUT,2771_OUT,2770_OUT,2769_OUT,2768_OUT,2767_OUT,2766_OUT,2765_OUT,2764_OUT,2763_OUT,2762_OUT,2761_OUT,2760_OUT,2759_OUT,2758_OUT,2757_OUT,2756_OUT,2755_OUT,2754_OUT,2753_OUT,2752_OUT,2751_OUT,2750_OUT,2749_OUT,2748_OUT,2747_OUT,2746_OUT,2745_OUT,2744_OUT,2743_OUT,2742_OUT,2741_OUT,2740_OUT,2739_OUT,2738_OUT,2737_OUT,2736_OUT,2735_OUT,2734_OUT,2733_OUT,2732_OUT,2731_OUT,2730_OUT,2729_OUT,2728_OUT,2727_OUT,2726_OUT,2725_OUT,2724_OUT,2723_OUT,2722_OUT,2721_OUT,2720_OUT,2719_OUT,2718_OUT,2717_OUT,2716_OUT,2715_OUT,2714_OUT,2713_OUT,2712_OUT,2711_OUT,2710_OUT,2709_OUT,2708_OUT,2707_OUT,27_OUT,26_OUT,25_OUT,24_OUT,2328_OUT,2327_OUT,232_OUT,2303_OUT,2302_OUT,2301_OUT,23_OUT,2299_OUT,2298_OUT,2296_OUT,2295_OUT,229_OUT,2288_OUT,2287_OUT,2286_OUT,228_OUT,227_OUT,2259_OUT,2258_OUT,2257_OUT,2256_OUT,2237_OUT,2236_OUT,2235_OUT,2203_OUT,2202_OUT,2201_OUT,2200_OUT,22_OUT,2196_OUT,2195_OUT,2185_OUT,2184_OUT,2183_OUT,2182_OUT,2181_OUT,2180_OUT,2179_OUT,2178_OUT,2177_OUT,2176_OUT,2175_OUT,21_OUT,205_OUT,204_OUT,203_OUT,202_OUT,201_OUT,200_OUT,20_OUT,2_OUT,199_OUT,197_OUT,196_OUT,195_OUT,1945_OUT,1944_OUT,1943_OUT,1940_OUT,194_OUT,1939_OUT,1938_OUT,1937_OUT,1930_OUT,193_OUT,1929_OUT,1928_OUT,1927_OUT,1926_OUT,1925_OUT,1924_OUT,1923_OUT,1922_OUT,1921_OUT,192_OUT,1916_OUT,1915_OUT,1914_OUT,1911_OUT,1910_OUT,1903_OUT,1902_OUT,19_OUT,1882_OUT,1881_OUT,1877_OUT,1876_OUT,1873_OUT,1872_OUT,1871_OUT,1861_OUT,1860_OUT,186_OUT,185_OUT,184_OUT,183_OUT,182_OUT,18_OUT,1736_OUT,1735_OUT,1734_OUT,1731_OUT,1730_OUT,1729_OUT,1728_OUT,1727_OUT,1726_OUT,1725_OUT,1724_OUT,1723_OUT,1722_OUT,1721_OUT,1720_OUT,1719_OUT,1718_OUT,1717_OUT,1716_OUT,1715_OUT,1714_OUT,1713_OUT,1712_OUT,1711_OUT,1710_OUT,1709_OUT,1708_OUT,1707_OUT,1706_OUT,1705_OUT,1704_OUT,1703_OUT,1702_OUT,1701_OUT,1700_OUT,17_OUT,1699_OUT,1698_OUT,1697_OUT,1696_OUT,1695_OUT,1694_OUT,1693_OUT,1692_OUT,1691_OUT,1690_OUT,1689_OUT,1688_OUT,1687_OUT,1686_OUT,1685_OUT,1684_OUT,1683_OUT,1682_OUT,1681_OUT,1680_OUT,1679_OUT,1678_OUT,1677_OUT,1676_OUT,1675_OUT,1674_OUT,1673_OUT,1672_OUT,1671_OUT,1670_OUT,1669_OUT,1668_OUT,1667_OUT,1666_OUT,1665_OUT,1664_OUT,1663_OUT,1662_OUT,1661_OUT,1660_OUT,1659_OUT,1658_OUT,1657_OUT,1656_OUT,1655_OUT,1654_OUT,1653_OUT,1652_OUT,1651_OUT,1650_OUT,165_OUT,1649_OUT,1648_OUT,1647_OUT,1646_OUT,1645_OUT,1644_OUT,1643_OUT,1642_OUT,1641_OUT,1640_OUT,164_OUT,1639_OUT,1638_OUT,1637_OUT,1636_OUT,1635_OUT,1634_OUT,1633_OUT,1632_OUT,1631_OUT,1630_OUT,,1620_OUT,162_OUT,1619_OUT,1618_OUT,1617_OUT,1616_OUT,1615_OUT,1614_OUT,1613_OUT,1612_OUT,1611_OUT,1610_OUT,1609_OUT,1608_OUT,1607_OUT,1606_OUT,1605_OUT,1604_OUT,1603_OUT,1602_OUT,1601_OUT,1600_OUT,160_OUT,16_OUT,1599_OUT,1598_OUT,1597_OUT,1596_OUT,1595_OUT,1594_OUT,1593_OUT,1592_OUT,1591_OUT,1590_OUT,159_OUT,1589_OUT,1588_OUT,1587_OUT,1586_OUT,1585_OUT,1584_OUT,1583_OUT,1582_OUT,1581_OUT,1580_OUT,158_OUT,1579_OUT,1578_OUT,1577_OUT,1576_OUT,1575_OUT,1574_OUT,1573_OUT,1572_OUT,1571_OUT,1570_OUT,1569_OUT,1568_OUT,1567_OUT,1566_OUT,1565_OUT,1564_OUT,1563_OUT,1562_OUT,1561_OUT,1560_OUT,1559_OUT,1558_OUT,1557_OUT,1556_OUT,1555_OUT,1554_OUT,1553_OUT,1552_OUT,1551_OUT,1550_OUT,1549_OUT,1548_OUT,1547_OUT,1546_OUT,1545_OUT,1544_OUT,1543_OUT,1542_OUT,1541_OUT,1540_OUT,1539_OUT,1538_OUT,1537_OUT,1536_OUT,1535_OUT,1534_OUT,1533_OUT,1532_OUT,1531_OUT,1530_OUT,1529_OUT,1528_OUT,1527_OUT,1526_OUT,1525_OUT,1524_OUT,1523_OUT,1522_OUT,1521_OUT,1520_OUT,1519_OUT,1518_OUT,1517_OUT,1516_OUT,1515_OUT,1514_OUT,1513_OUT,1512_OUT,1511_OUT,1510_OUT,1509_OUT,1508_OUT,1507_OUT,1506_OUT,1505_OUT,1504_OUT,1503_OUT,1502_OUT,1501_OUT,1500_OUT,15_OUT,1499_OUT,1498_OUT,1497_OUT,1496_OUT,1495_OUT,1494_OUT,1493_OUT,1492_OUT,1491_OUT,1490_OUT,1489_OUT,1488_OUT,1468_OUT,1467_OUT,1466_OUT,1465_OUT,1464_OUT,1463_OUT,1462_OUT,1461_OUT,1460_OUT,1459_OUT,142_OUT,141_OUT,140_OUT,14_OUT,139_OUT,138_OUT,137_OUT,136_OUT,135_OUT,134_OUT,133_OUT,132_OUT,131_OUT,130_OUT,13_OUT,129_OUT,128_OUT,127_OUT,126_OUT,125_OUT,124_OUT,123_OUT,122_OUT,121_OUT,120_OUT,12_OUT,119_OUT,118_OUT,117_OUT,116_OUT,115_OUT,114_OUT,113_OUT,112_OUT,111_OUT,110_OUT,11_OUT,109_OUT,108_OUT,107_OUT,106_OUT,105_OUT,104_OUT,103_OUT,102_OUT,101_OUT,100_OUT,10_OUT,1_OUT,163_OUT,1629_OUT,1628_OUT,1627_OUT,1626_OUT,1625_OUT,1624_OUT,1623_OUT,1622_OUT,1621_OUT"
out_string_parsed = out_string.replace("_OUT","")
out_list = out_string_parsed.split(',')
print len(out_list)



with open(report_file, 'w') as wf:
    for log_file in log_files:
        from_location_list = []
        to_location_list = []
        path_to, the_file_name = ntpath.split(log_file)
        f_in = open(log_file, 'rb')
        try:
            reader = csv.reader(f_in)
            for row in reader:
                from_location = row[0].replace("_OUT", "")
                to_location = row[1].replace("_IN", "")
#                from_location = row[0]
#                to_location = row[1]

                
                if from_location in out_list and from_location not in from_location_list:
                    wf.write(str(the_file_name+","+from_location+'\n'))
                    from_location_list.append(from_location)
                    
                if to_location in out_list and to_location not in to_location_list:
                    wf.write(str(the_file_name+","+to_location+'\n'))
                    to_location_list.append(to_location)
                    
        finally:
            f_in.close()
           

#
##    f_out = open(report_file, 'wb')
##    writer = csv.writer(f_out)
#with open(report_file, 'w') as wf:
#    for log_file in log_files:
#        path_to, the_file_name = ntpath.split(log_file)
#        f_in = open(log_file, 'rb')
#        try:
#            reader = csv.reader(f_in)
#            for row in reader:
##                from_location = row[0].replace("_OUT", "")
##                to_location = row[1].replace("_IN", "")
#                from_location = row[0]
#                to_location = row[1]
#                
##                if not from_location in from_location_list:
##                    from_location_list.append(from_location)
###                    writer.writerow(str(from_location))
##                    wf.write(str(from_location+'\n'))
##                if not to_location in to_location_list:
##                    to_location_list.append(to_location)
###                    writer.writerow(str(to_location))
##                    wf.write(str(to_location+'\n'))
#                
#                if not from_location in location_list:
#                    location_list.append(from_location)
##                    writer.writerow(str(from_location))
#                    wf.write(str(the_file_name+","+from_location+'\n'))
#                if not to_location in location_list:
#                    location_list.append(to_location)
##                    writer.writerow(str(to_location))
#                    wf.write(str(the_file_name+","+to_location+'\n'))
#                
#        finally:
#            f_in.close()
#           

