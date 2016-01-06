SELECT count(*) FROM (
	select docid from Frequency group by docid having count(term) > 300
);

