select sum(a.count*b.count) from Frequency a, Frequency b where a.docid='10080_txt_crude' and b.docid='17035_txt_earn' and a.term=b.term;
