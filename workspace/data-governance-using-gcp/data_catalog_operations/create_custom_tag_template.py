from google.cloud import datacatalog_v1

client = datacatalog_v1.DataCatalogClient()

template = datacatalog_v1.TagTemplate()
template.display_name = "Compliance Metadata"

sensitivity_level_field = datacatalog_v1.TagTemplateField()
sensitivity_level_field.display_name="Sensitivity Level"
sensitivity_level_field.type_.enum_type.allowed_values.extend([
    datacatalog_v1.FieldType.EnumType.EnumValue(display_name="Public"),
    datacatalog_v1.FieldType.EnumType.EnumValue(display_name="Internal"),
    datacatalog_v1.FieldType.EnumType.EnumValue(display_name="Confidential"),
    datacatalog_v1.FieldType.EnumType.EnumValue(display_name="Restricted")
])
template.fields["sensitivity_level"] = sensitivity_level_field

template.fields["data_owner"] =  datacatalog_v1.TagTemplateField(display_name="Data Owner",
                                                                 type=datacatalog_v1.FieldType(primitive_type=datacatalog_v1.FieldType.PrimitiveType.STRING))


project_id = "upgradlabs-1735976404499"
tmplate_id = "compliance_metadata"

client.create_tag_template(parent=f"projects/{project_id}/locations/us-east1",
                           tag_template_id=tmplate_id,
                           tag_template=template)
print("created")

