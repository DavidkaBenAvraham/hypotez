
drop trigger if exists `hypotez2shalom_after_insert_hypotez_cms`;
CREATE  TRIGGER IF NOT EXISTS `hypotez2shalom_after_insert_hypotez_cms` AFTER
INSERT
	ON
	`hypotez_cms`
FOR EACH ROW BEGIN
INSERT
INTO
	`shalom_cms` 
   (
	`id_cms`,
	`id_cms_category`,
	`position`,
	`active`,
	`indexation`
)
values
(
	NEW.id_cms,
	NEW.id_cms_category,
	NEW.`position`,
	NEW.`active`,
	NEW.indexation
);
end;


delimiter |
CREATE  TRIGGER IF NOT EXISTS `hypotez2shalom_after_update_hypotez_cms` AFTER
UPDATE
	ON
	`hypotez_cms`
FOR EACH ROW BEGIN
UPDATE 
	`shalom_cms` 
   SET
	`id_cms` = NEW.id_cms,
	`id_cms_category` = NEW.id_cms_category,
	`position` = NEW.`position`,
	`active` = NEW.active,
	`indexation` = NEW.indexation
|

delimiter |
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_cms` AFTER
	DELETE 
	ON
	`hypotez_cms`
FOR EACH ROW BEGIN
   DELETE FROM  shalom_cms 
   WHERE `id_cms` = OLD.id_cms;
   END;
	
	|