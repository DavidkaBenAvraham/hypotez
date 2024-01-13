
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_quick_access` AS
select
   *
from
    `hypotez_quick_access`
;
    


CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_quick_access_lang` AS
select
   *
from
    `hypotez_quick_access_lang`;
    


drop table if exists shalom_currency;
create table if not exists shalom_currency like hypotez_currency;
insert into shalom_currency select * from hypotez_currency;


drop table if exists shalom_currency_lang;
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_currency_lang` AS
select
   *
from
    `hypotez_currency_lang`;
   
   
drop table if exists shalom_currency_shop;
create table if not exists shalom_currency_shop like hypotez_currency_shop;
insert into shalom_currency_shop select * from hypotez_currency_shop ;

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_currency_shop` AS
select
   *
from
    `hypotez_currency_shop`;
   
drop table if exists shalom_tax;
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_tax` AS
select
   *
from
    `hypotez_tax`;   

   
drop table if exists shalom_tax_lang;
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_tax_lang` AS
select
   *
from
    `hypotez_tax_lang`;   
   
drop table if exists shalom_tax_rule;
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `shalom_tax_rule` AS
select
   *
from
    `hypotez_tax_rule`;   

   
