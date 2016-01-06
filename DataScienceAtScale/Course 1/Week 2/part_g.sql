SELECT SUM(a.value*b.value)
	FROM a, b
	WHERE a.col_num = b.row_num
	GROUP BY a.row_num, b.col_num HAVING a.row_num=2 and b.col_num=3;
