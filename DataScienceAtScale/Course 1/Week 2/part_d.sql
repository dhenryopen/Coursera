SELECT count(*) FROM (
  select distinct(docid) FROM (
	select distinct(docid) from Frequency where term = 'law' 
		UNION	
	select distinct(docid) from Frequency where term = 'legal' 
  )
);
