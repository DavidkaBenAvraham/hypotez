
drop table if exists `e_cat_product` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product` AS
select
   *
from
    `shalom_phones_product`;
	
	
drop table if exists `e_cat_product_attachment` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_attachment` AS
select
   *
from
    `shalom_phones_product_attachment`;
	
	
drop table if exists `e_cat_product_attribute` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_attribute` AS
select
   *
from
    `shalom_phones_product_attribute`;
	
	
drop table if exists `e_cat_product_attribute_combination` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_attribute_combination` AS
select
   *
from
    `shalom_phones_product_attribute_combination`;
	
	
	
drop table if exists `e_cat_product_attribute_image` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_attribute_image` AS
select
   *
from
    `shalom_phones_product_attribute_image`;
	
	
drop table if exists `e_cat_product_attribute_shop` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_attribute_shop` AS
select
   *
from
    `shalom_phones_product_attribute_shop`;
	
	
	
drop table if exists `e_cat_product_carrier` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_carrier` AS
select
   *
from
    `shalom_phones_product_carrier`;
	
	
drop table if exists `e_cat_product_comment` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment` AS
select
   *
from
    `shalom_phones_product_comment`;
	
	
	
drop table if exists `e_cat_product_comment_criterion` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_criterion` AS
select
   *
from
    `shalom_phones_product_comment_criterion`;
	
	
	
drop table if exists `e_cat_product_comment_criterion_category` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_criterion_category` AS
select
   *
from
    `shalom_phones_product_comment_criterion_category`;
	
	
drop table if exists `e_cat_product_comment_criterion_lang` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_criterion_lang` AS
select
   *
from
    `shalom_phones_product_comment_criterion_lang`;
	
	
drop table if exists `e_cat_product_comment_criterion_product` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_criterion_product` AS
select
   *
from
    `shalom_phones_product_comment_criterion_product`;
	
	
	
drop table if exists `e_cat_product_comment_grade` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_grade` AS
select
   *
from
    `shalom_phones_product_comment_grade`;
	
	
	
drop table if exists `e_cat_product_comment_report` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_report` AS
select
   *
from
    `shalom_phones_product_comment_report`;
	
	
	
drop table if exists `e_cat_product_comment_usefulness` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_comment_usefulness` AS
select
   *
from
    `shalom_phones_product_comment_usefulness`;
	
	
drop table if exists `e_cat_product_country_tax` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_country_tax` AS
select
   *
from
    `shalom_phones_product_country_tax`;
	
	
drop table if exists `e_cat_product_download` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_download` AS
select
   *
from
    `shalom_phones_product_download`;
	
	
	
drop table if exists `e_cat_product_group_reduction_cache` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_group_reduction_cache` AS
select
   *
from
    `shalom_phones_product_group_reduction_cache`;
	
	
	
drop table if exists `e_cat_product_lang` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_lang` AS
select
   *
from
    `shalom_phones_product_lang`;
	
	
drop table if exists `e_cat_product_sale` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_sale` AS
select
   *
from
    `shalom_phones_product_sale`;
	
	
drop table if exists `e_cat_product_shop` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_shop` AS
select
   *
from
    `shalom_phones_product_shop`;
	
	
drop table if exists `e_cat_product_supplier` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_supplier` AS
select
   *
from
    `shalom_phones_product_supplier`;
	
	
drop table if exists `e_cat_product_tag` ; 
CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `e_cat_product_tag` AS
select
   *
from
    `shalom_phones_product_tag`;