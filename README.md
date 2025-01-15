# Webcrawler-IP-subnets-aggregating-and-blocking

**Step 1: go to the right directory and run python3 log_analyzer.py
**
**Step 2: Copy the result to an excel and build a formula like this:
**
# of ips	range	ufw statement formula		Below are just copied text from column C
77	111.225.148	ufw insert 1 deny from 111.225.148.0/24;		ufw insert 1 deny from 101.47.11.0/24;
77	111.225.149	ufw insert 1 deny from 111.225.149.0/24;		ufw insert 1 deny from 101.67.29.0/24;
77	110.249.202	ufw insert 1 deny from 110.249.202.0/24;		ufw insert 1 deny from 102.164.58.0/24;
73	110.249.201	ufw insert 1 deny from 110.249.201.0/24;		ufw insert 1 deny from 106.8.136.0/24;
34	101.67.29	ufw insert 1 deny from 101.67.29.0/24;		ufw insert 1 deny from 106.8.139.0/24;
32	106.8.139	ufw insert 1 deny from 106.8.139.0/24;		ufw insert 1 deny from 110.249.201.0/24;
30	57.141.7	ufw insert 1 deny from 57.141.7.0/24;		ufw insert 1 deny from 110.249.202.0/24;
28	106.8.136	ufw insert 1 deny from 106.8.136.0/24;		ufw insert 1 deny from 111.225.148.0/24;
25	60.188.9	ufw insert 1 deny from 60.188.9.0/24;		ufw insert 1 deny from 111.225.149.0/24;
24	112.13.112	ufw insert 1 deny from 112.13.112.0/24;		ufw insert 1 deny from 112.13.112.0/24;
![image](https://github.com/user-attachments/assets/632d202a-6328-4a22-9b89-e7fbb725552e)

**Step 3: run the list in Linux to block all these subnets:
**For example:
ufw insert 1 deny from 101.47.11.0/24;
ufw insert 1 deny from 101.67.29.0/24;
ufw insert 1 deny from 102.164.58.0/24;
ufw insert 1 deny from 106.8.136.0/24;
ufw insert 1 deny from 106.8.139.0/24;
ufw insert 1 deny from 110.249.201.0/24;
ufw insert 1 deny from 110.249.202.0/24;
ufw insert 1 deny from 111.225.148.0/24;
ufw insert 1 deny from 111.225.149.0/24;
ufw insert 1 deny from 112.13.112.0/24;
![image](https://github.com/user-attachments/assets/8c12dffa-192d-445e-916e-fb3db7f935f4)


