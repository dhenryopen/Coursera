select distinct sum(a.count*b.count) "similarity" from searchFrequency a, searchFrequency b where a.term=b.term group by a.docid, b.docid having a.docid='q' order by similarity;
