## Introduction

YAML stands for "**YAML Ain't Markup Language**." It is a human-readable **data serialization language** that is often used for configuration files and data exchange between different programming languages.


> 💡 Markup languages are used to structure, format or define relationship between parts of a document.



![image](https://github.com/user-attachments/assets/66c75a0c-466a-4eb9-b1a6-02c86265c6e3)


## Benefits of Yaml

- It is an Serialization language like **JSON** & **XML**
- Configuration files are written in yaml. **eg:** Docker and Kubernetes , logs ,caches
- Standard format to transfer data.
- File extension: **`.yml  .yaml`**
- Yaml use line separation and indentation.


> 💡 YAML is a superset of JSON . any valid JSON file is also a valid YAML File.

<br>

### Serialization & Deserialization

- **Serialization** is a way to convert data structures into a format that can be easily stored or transferred. It's like packing your clothes into a suitcase before traveling. In the case of YAML, it's a way to represent data structures in a human-readable text format.
- **Deserialization** is the opposite process of serialization. It's like unpacking your clothes from the suitcase after arriving at your destination. In the case of YAML, it's the process of converting human-readable text format back into data structures that computers can understand.

### Components of YAML files

```yaml
--- #Means Contains more than one yaml document or yaml files separator

... #Means Document Finished

# Comments
```

**Key :** Value Pairs - In yaml everything should be in key, value pairs.

```yaml
eg: app: user-demo #if we use special characters we give string values in quotes.
    port:9000
    version:1.7
```

**Objects :** YAML object representing a person's information with name, age, and city as key-value pairs.

```yaml
eg: Person:
     name: John Smith, age: 30, city: New York #object attributes
```

**Lists :** In YAML, you can represent a list (or array) using hyphens "-" for each item.

```yaml
eg: Microservices:       #list
       - app:demo        #item of the list
         version: 1.7
       - app: production
         version: 1.8
# Nested list
     eg: Microservices:       #list
       - app:demo             #item of the list
         version: 
             - 1.7
             - 1.8            #items of the nestedlist
 [ 0R ]
         version : [1.7,1.8]  #both are same
```

**Booleans :** Boolean values in yaml are
- True / False
- Yes / No
- on / off

```yaml
eg: microservices:
       deployed: yes
```

**Multiline Strings :** Used in shell script to execute commands one by one in a list format

```yaml
eg: Multilinestring : | (pipe symbol)
      demo app
      can deploy later

eg: Singleline : > (consider as singleline)
      demo app
      can deploy later
```

**Environment variables :** Environment variables store configuration settings and other important information for programs and processes running on a computer. They are typically key-value pairs, where the key is the variable name and the value is the associated data.
Using ($) we can access the environment variables.

```bash
eg: database:
		   host: localhost
		   port: 5432
		   username: $DB_USERNAME
		   password: $DB_PASSWORD
```

**Placeholders:**

```yaml
eg: database:
       host: localhost
       port: 5432
       username: {{DB_USERNAME}}
       password: {{DB_PASSWORD}}
```

### Datatypes in YAML

**1. String Variables** -
``` yaml  
   eg: Myself : "Raghul M"
       job : SQE intern
       Cmpy : Redhat
```

**2. Numbers & Boolean** -

```yaml
   eg:
        marks : 800     #int type
        average : 8.5   #float type
        pass  : True    #Boolean type
        # Specifying the type 
        zero : !!int 0
        pass_num : !!int 45
        commasep_val : !!int +540_000 #540,000
        Pass : !!bool true
        infinite : .naf
        notanum : .nan
        floatval : !!float 56.63
        ~ : !!null NULL     #null value
        date : !!timestop 2022-09-25   # Date type 
```

**3. Sequence or List** -
```yaml
   eg: student : !!seq
         - raghul
         - 21
```

**4. Maps** - Key:value pairs are called maps. and Nested Mapping map within a map
```yaml
   eg: database:
         host: localhost
         port: 5432
         username: $DB_USERNAME
         password: $DB_PASSWORD #we also give these values in {a:b,c:d}
```

**5. Pairs** - Keys may have duplicate values
```yaml
   eg: employee_type : !!pairs
          -job : intern
          -job : fulltime
[ OR ]

      employee_type : !!pairs[job : intern,job : fulltime]
```

**6. Set** - It allow only unique values
```yaml
   eg: names: !!set
         ? Raghul
         ? Tesla
```

**7. OMap** - In YAML, !!omap represents an ordered map that maintains the order of its key-value pairs 
	 based on the order in which they were added, allowing you to iterate through the entries in the 
   order they were defined.
```yaml
   eg: Imported: !!omap
          - key1: value1
          - key2: value2
          - key3: value3
```

 **8. Reusing Properties** - The ampersand `(&)` character is used to define an anchor, which is a reference
    point for a set of properties. The asterisk `(*)` character is used to reference the properties 
    from the anchor. This allows for the reuse of properties within the YAML document.
```yaml
eg: person: &details
    name: John
    age: 30				
    friend:
        <<: *details
      name: Alice
```

**Example YAML File:**
```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest

    
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.12.12
      with:
          heroku_api_key: ${{secrets.HEROKU_API_TOKEN}}
          heroku_app_name: ${{secrets.HEROKU_APP_NAME}} #Must be unique in Heroku
          heroku_email: "demo@gmail.com"
```
