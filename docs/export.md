# Vault: export

Exporting items is easy. You just have to use the flag `--export`.

## Usage

```
./vault.py --export path/to/file.json
```

## Export sample

Files are exported at the following format:

```json
[
	{
		"categoryName": "Perso",
		"name": "some item",
		"login": "gab@notarealemail.com",
		"password": "password1",
		"notes": "my notes\nmore notes"
	},
	{
		"categoryName": "Pro",
		"name": "some other item",
		"login": "one@notarealemail.com",
		"password": "password2",
		"notes": "notes"
	},
	{
		"categoryName": "new category for import",
		"name": "another kind of item",
		"login": "two@notarealemail.com",
		"password": "password3 is very complicated!",
		"notes": "sdasd"
	},
	{
		"categoryName": "Perso",
		"name": "my stuff",
		"login": "three@notarealemail.com",
		"password": "password4 is even more complicated!",
		"notes": ""
	},
	{
		"categoryName": "n/a",
		"name": "multi line item",
		"login": "foor@notarealemail.com",
		"password": "password5",
		"notes": "multi\nline\nitem"
	}
]
```