import json, re

with open('data/questions_rpl.js', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find('[')
e = text.rfind(']')
items = json.loads(text[s:e+1])

# Clean Java code snippet
clean_java = """```java
class Pegawai {
    public void kerja() {
        System.out.println("Pegawai bekerja");
    }
}

class Programmer extends Pegawai {
    @Override
    public void kerja() {
        System.out.println("Programmer coding");
    }
}

public class Main {
    public static void main(String[] args) {
        Pegawai p = new Programmer();
        p.kerja();
    }
}
```"""

# Clean SQL snippet
clean_sql = """```sql
SELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai
FROM siswa
WHERE status = 'aktif'
GROUP BY jurusan
HAVING AVG(nilai) >= 80.0;
```"""

# Clean JS snippet
clean_js = """```javascript
console.log('1');

setTimeout(() => {
    console.log('2');
}, 0);

Promise.resolve().then(() => {
    console.log('3');
});

console.log('4');
```"""

updated_count = 0
for q in items:
    content = q.get('questionHtml', q.get('question', ''))
    if 'class Pegawai' in content:
        # replace the old ```java ... ``` block with clean_java
        new_content = re.sub(r'```java[\s\S]*?```', clean_java, content)
        q['questionHtml'] = new_content
        updated_count += 1
    elif 'SELECT jurusan' in content:
        new_content = re.sub(r'```sql[\s\S]*?```', clean_sql, content)
        q['questionHtml'] = new_content
        updated_count += 1
    elif 'console.log(\'1\')' in content or "console.log('1')" in content:
        new_content = re.sub(r'```javascript[\s\S]*?```', clean_js, content)
        q['questionHtml'] = new_content
        updated_count += 1

print(f'Updated {updated_count} questions in questions_rpl.js')

output_js = '/**\n * TKA MASTERY HUB — QUESTIONS_RPL.JS (135 SOAL AUTENTIK)\n */\nwindow.TKA_RPL_QUESTIONS = ' + json.dumps(items, indent=2, ensure_ascii=False) + ';\n'

with open('data/questions_rpl.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print('Successfully saved data/questions_rpl.js')
