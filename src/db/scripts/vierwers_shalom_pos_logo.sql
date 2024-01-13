DROP TABLE IF EXISTS shalom_pos_logo;
CREATE  OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_pos_logo` AS
select
   *
from
    `hypotez_pos_logo`;
   
   
DROP TABLE IF EXISTS shalom_pos_logo_shop;
CREATE  OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_pos_logo_shop` AS
select
   *
from
    `hypotez_pos_logo_shop`;