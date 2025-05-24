import json

input_file = 'openapi.json'
output_file = 'openapi_cleaned.json'

with open(input_file) as f:
    spec = json.load(f)

if 'tags' in spec:
    seen = set()
    unique_tags = []
    for tag in spec['tags']:
        tag_name = tag.get('name')
        if tag_name and tag_name not in seen:
            unique_tags.append(tag)
            seen.add(tag_name)
    spec['tags'] = unique_tags
    print(f"✅ Deduplicated top-level tags: kept {len(unique_tags)} unique tags")
else:
    print("⚠️ No top-level 'tags' section found in the spec")

with open(output_file, 'w') as f:
    json.dump(spec, f, indent=2)

print(f"✅ Saved cleaned spec to {output_file}")
