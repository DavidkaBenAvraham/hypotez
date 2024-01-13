ALTER TABLE `e_cat_product_lang` ADD COLUMN IF NOT EXISTS `Open AI Product Description` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_short_link` NVARCHAR(128)  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_text` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN IF NOT EXISTS `affiliate_summary` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_summary_2` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `byer_protection` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Open AI Product Description` TEXT  NULL DEFAULT NULL;
ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_short_link` NVARCHAR(128)  NULL DEFAULT NULL;
ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_text` TEXT  NULL DEFAULT NULL;
ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_summary` TEXT  NULL DEFAULT NULL;
ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `affiliate_summary_2` TEXT  NULL DEFAULT NULL;
ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `byer_protection` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Specifiaction` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Specifiaction` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Ref product description` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Ref product description` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Additional shipping details` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Additional shipping details` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Product features` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Product features` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Refirbished product description` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Refirbished product description` TEXT  NULL DEFAULT NULL;

ALTER TABLE `shalom_phones_product_lang` ADD COLUMN  IF NOT EXISTS `Additional product info` TEXT  NULL DEFAULT NULL;
ALTER TABLE `e_cat_product_lang` ADD COLUMN  IF NOT EXISTS `Additional product info` TEXT  NULL DEFAULT NULL;
