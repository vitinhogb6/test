import avro.schema

# Open the Avro schema file
with open('example.avsc', 'rb') as f:
    schema_str = f.read()

# Parse the schema
schema = avro.schema.Parse(schema_str)

# Print the schema
print(schema)
