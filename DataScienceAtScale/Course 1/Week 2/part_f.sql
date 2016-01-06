SELECT count(*) FROM (
  select distinct(docid) FROM (
	select distinct(docid) from Frequency where term = 'transactions' 
		INTERSECT	
	select distinct(docid) from Frequency where term = 'world' 
  )
);
