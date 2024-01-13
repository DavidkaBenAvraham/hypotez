	/*
	delete from `shalom_pos_logo`;
	delete from `shalom_pos_logo_shop`;
	INSERT INTO `shalom_pos_logo` SELECT * FROM `hypotez_pos_logo`;
	INSERT INTO `shalom_pos_logo_shop` SELECT * FROM `hypotez_pos_logo_shop`;
	*/

	{ CALL u177424397_DEV.`COPY pos_logo hypotez2shalom`() }
	