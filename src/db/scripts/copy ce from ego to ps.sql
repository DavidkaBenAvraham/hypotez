/*
delete from hypotez_category;
insert into hypotez_category select * from ego_category;

delete from hypotez_category_group;
insert into hypotez_category_group select * from ego_category_group;

delete from hypotez_category_lang;
insert into hypotez_category_lang select * from ego_category_lang;

delete from hypotez_category_product;
insert into hypotez_category_product select * from ego_category_product;

delete from hypotez_category_shop;
insert into hypotez_category_shop select * from ego_category_shop;
*/



delete from ps_ce_content;
insert into ps_ce_content 
select * from ego_ce_content;



delete from ps_ce_content_lang;
insert into ps_ce_content_lang 
select * from ego_ce_content_lang;
/*
delete from ps_ce_content_lang ; -- where `id_shop` = 3;
insert into ps_ce_content_lang (
`id_ce_content`,
`id_lang`,
`id_shop`,
`title`,
`content`)

select

`id_ce_content`,
`id_lang`,
`id_shop`,
`title`,
`content`
 from ego_ce_content_lang
;
*/

delete from ps_ce_content_shop;
insert into ps_ce_content_shop 
select * from ego_ce_content_shop;
/*
delete from ps_ce_content_shop ; -- where `id_shop` = 3;
insert into 
ps_ce_content_shop (
`id_ce_content`,
`id_shop`,
`position`,
`active`,
`date_add`,
`date_upd`)
select 
`id_ce_content`,
`id_shop`,
`position`,
`active`,
`date_add`,
`date_upd`
from ego_ce_content_shop;
*/

delete from ps_ce_meta;
insert into ps_ce_meta 
select * from ego_ce_meta;


delete from ps_ce_revision;
insert into ps_ce_revision 
select * from ego_ce_revision;





delete from ps_ce_template;

insert into ps_ce_template
(
`id_ce_template`,
`id_employee`,
`title`,
`type`,
`content`,
`position`,
`active`,
`date_add`,
`date_upd`)
SELECT `id_ce_template`,
`id_employee`,
`title`,
`type`,
`content`,
`position`,
`active`,
`date_add`,
`date_upd`
from ego_ce_template;














delete from ps_ce_theme;

insert into ps_ce_theme
(
`id_ce_theme`,
`id_employee`,
`type`,
`position`,
`active`,
`date_add`,
`date_upd`)
SELECT`id_ce_theme`,
`id_employee`,
`type`,
`position`,
`active`,
`date_add`,
`date_upd`
from ego_ce_theme;





delete from ps_ce_theme_lang;
insert into ps_ce_theme_lang 
select * from ego_ce_theme_lang;

delete from ps_ce_theme_lang ; -- where `id_shop` = 3 ;
/* -1- */
insert into ps_ce_theme_lang
(
`id_ce_theme`,
`id_lang`,
`id_shop`,
`title`,
`content`)
SELECT `id_ce_theme`,
`id_lang`,
1,
`title`,
`content`
from ego_ce_theme_lang; 
/* -2- */
insert into ps_ce_theme_lang
(
`id_ce_theme`,
`id_lang`,
`id_shop`,
`title`,
`content`)
SELECT `id_ce_theme`,
`id_lang`,
2,
`title`,
`content`
from ego_ce_theme_lang;
/* -3- */
insert into ps_ce_theme_lang
(
`id_ce_theme`,
`id_lang`,
`id_shop`,
`title`,
`content`)
SELECT `id_ce_theme`,
`id_lang`,
3,
`title`,
`content`
from ego_ce_theme_lang;-- where `id_ce_theme` = 17 or `id_ce_theme` = 18;




delete from ps_ce_theme_shop ; -- where `id_shop` = 3 ;

insert into ps_ce_theme_shop
(
`id_ce_theme`,
`id_shop`,
`position`,
`active`,
`date_add`,
`date_upd`)
SELECT 
`id_ce_theme`,
`id_shop`,
`position`,
`active`,
`date_add`,
`date_upd`

from ego_ce_theme_shop
where `id_shop` = 3;


