
delimiter |
CREATE TRIGGER `after_insert_hypotez_product` AFTER
INSERT
	ON
	`hypotez_product`
FOR EACH ROW BEGIN
   INSERT
	INTO
	`shalom_product` Set 
	`id_product` = NEW.id_product,
	`id_supplier` = NEW.id_supplier,
	`id_manufacturer` = NEW.id_manufacturer,
	`id_category_default` = NEW.id_category_default,
	`id_shop_default` = NEW.id_shop_default,
	`id_tax` = NEW.id_tax,
	`on_sale` = NEW.on_sale,
	`online_only` = NEW.online_only,
	`ean13` = NEW.ean13,
	`isbn` = NEW.isbn,
	`upc` = NEW.upc,
	`mpn` = NEW.mpn,
	`ecotax` = NEW.ecotax,
	`quantity` = NEW.quantity,
	`minimal_quantity` = NEW.minimal_quantity,
	`low_stock_threshold` = NEW.low_stock_threshold,
	`low_stock_alert` = NEW.low_stock_alert,
	`price` = NEW.price,
	`wholesale_price` = NEW.wholesale_price,
	`unity` = NEW.unity,
	`unit_price_ratio` = NEW.unit_price_ratio,
	`additional_shipping_cost` = NEW.additional_shipping_cost,
	`reference` = NEW.reference,
	`supplier_reference` = NEW.supplier_reference,
	`location` = NEW.location,
	`width` = NEW.width,
	`height` = NEW.height,
	`depth` = NEW.depth,
	`weight` = NEW.weight,
	`out_of_stock` = NEW.out_of_stock,
	`additional_delivery_times` = NEW.additional_delivery_times,
	`quantity_discount` = NEW.quantity_discount,
	`customizable` = NEW.customizable,
	`uploadable_files` = NEW.uploadable_files,
	`text_fields` = NEW.text_fields,
	`active` = NEW.active,
	`redirect_type` = NEW.redirect_type,
	`id_type_redirected` = NEW.id_type_redirected,
	`available_for_order` = NEW.available_for_order,
	`available_date` = NEW.available_date,
	`show_condition` = NEW.show_condition,
	`condition` = NEW.condition,
	`show_price` = NEW.show_price,
	`indexed` = NEW.indexed,
	`visibility` = NEW.visibility,
	`cache_is_pack` = NEW.cache_is_pack,
	`cache_has_attachments` = NEW.cache_has_attachments,
	`is_virtual` = NEW.is_virtual,
	`cache_default_attribute` = NEW.cache_default_attribute,
	`date_add` = NEW.date_add,
	`date_upd` = NEW.date_upd,
	`advanced_stock_management` = NEW.advanced_stock_management,
	`pack_stock_type` = NEW.pack_stock_type,
	`state` = NEW.state,
	`product_type` = NEW.product_type;
	
   END;
   |
   


delimiter |
CREATE TRIGGER `after_update_hypotez_product` AFTER
UPDATE 
	ON
	`hypotez_product`
FOR EACH ROW BEGIN
   UPDATE 
	
	`shalom_product` Set 
	
	`id_supplier` = NEW.id_supplier,
	`id_manufacturer` = NEW.id_manufacturer,
	`id_category_default` = NEW.id_category_default,
	`id_shop_default` = NEW.id_shop_default,
	`id_tax` = NEW.id_tax,
	`on_sale` = NEW.on_sale,
	`online_only` = NEW.online_only,
	`ean13` = NEW.ean13,
	`isbn` = NEW.isbn,
	`upc` = NEW.upc,
	`mpn` = NEW.mpn,
	`ecotax` = NEW.ecotax,
	`quantity` = NEW.quantity,
	`minimal_quantity` = NEW.minimal_quantity,
	`low_stock_threshold` = NEW.low_stock_threshold,
	`low_stock_alert` = NEW.low_stock_alert,
	`price` = NEW.price,
	`wholesale_price` = NEW.wholesale_price,
	`unity` = NEW.unity,
	`unit_price_ratio` = NEW.unit_price_ratio,
	`additional_shipping_cost` = NEW.additional_shipping_cost,
	`reference` = NEW.reference,
	`supplier_reference` = NEW.supplier_reference,
	`location` = NEW.location,
	`width` = NEW.width,
	`height` = NEW.height,
	`depth` = NEW.depth,
	`weight` = NEW.weight,
	`out_of_stock` = NEW.out_of_stock,
	`additional_delivery_times` = NEW.additional_delivery_times,
	`quantity_discount` = NEW.quantity_discount,
	`customizable` = NEW.customizable,
	`uploadable_files` = NEW.uploadable_files,
	`text_fields` = NEW.text_fields,
	`active` = NEW.active,
	`redirect_type` = NEW.redirect_type,
	`id_type_redirected` = NEW.id_type_redirected,
	`available_for_order` = NEW.available_for_order,
	`available_date` = NEW.available_date,
	`show_condition` = NEW.show_condition,
	`condition` = NEW.condition,
	`show_price` = NEW.show_price,
	`indexed` = NEW.indexed,
	`visibility` = NEW.visibility,
	`cache_is_pack` = NEW.cache_is_pack,
	`cache_has_attachments` = NEW.cache_has_attachments,
	`is_virtual` = NEW.is_virtual,
	`cache_default_attribute` = NEW.cache_default_attribute,
	`date_add` = NEW.date_add,
	`date_upd` = NEW.date_upd,
	`advanced_stock_management` = NEW.advanced_stock_management,
	`pack_stock_type` = NEW.pack_stock_type,
	`state` = NEW.state,
	`product_type` = NEW.product_type
	
	where `id_product` = NEW.id_product;
	
   END;
   |
   


delimiter |
CREATE TRIGGER `after_delete_hypotez_product` AFTER
	DELETE 
	ON
	`hypotez_product`
FOR EACH ROW BEGIN
   DELETE FROM  shalom_product 
   WHERE `id_product` = OLD.id_product;
   END;
	
	|
