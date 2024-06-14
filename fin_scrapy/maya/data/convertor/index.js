

async function run() {

    const XLSX = require('xlsx')
    const fs = require('fs')
    const inputFilePath = `./datatest.xlsx`
    const outputFilePath = `./convert.json`
    const sheetName = 'datasheet'

    let buf = fs.readFileSync(inputFilePath);
    let workbook = XLSX.read(buf, { type: 'buffer' });
    const sheets = {}

    workbook.SheetNames.forEach(function (currentSheetName) {
        try{ 
            let sheet = XLSX.utils.sheet_to_json(workbook.Sheets[currentSheetName], { blankrows: false});

            sheets[currentSheetName] = sheet
        } catch(e) {
            console.error(e.message)
        }

        // combine all sheets to one sheet (in sheets obj):
        // sheets.push(sheet)
        // console.log(`***** ${sheetName} *****:`)
    })
    
    const sheet = sheets[sheetName]
    const file = []
    
    for (const row of sheet) {
        const keys = Object.keys(row)
        const years = keys
        .filter(i => i.indexOf('_') > -1)
        .reduce((acc, c) => {
            const year = c.split('_')[0]
            acc.add(year)
            return acc
        }, new Set())

        const data = { 
            "company": row['company'],
            "mayaid": row['mayaid'],
            "tckr": row['tckr'],
            "list": []
        }
        
        for (let year of years) {

            const yearWithUnderscore = year + '_'
            const listItem = keys.filter(i => i.startsWith(yearWithUnderscore)).reduce((acc,key)=> {
                const dataKey = key.substring(yearWithUnderscore.length)
                const dataValue = row[key]
                acc[dataKey] = dataValue
                return acc
            }, {})

            const qChar = '|' // TODO: repalce '|' with 'q'
            if (year.indexOf(qChar) > -1) {
                const [ yearName, qName ] = year.split(qChar)
                listItem['year'] = yearName
                listItem['q'] = qName
            } else {
                listItem['year'] = year
            }
            
            data.list.push(listItem)
        }
        file.push(data)
    }
    
    fs.writeFile(outputFilePath, JSON.stringify(file, null, 2), function(err) {
        if(err) {
            return console.log(err);
        }
    
        console.log("The file was saved!");
    }); 
}

try {
    console.log('---start ---')
    const result = run()
    console.log('---end ---')

} catch(e) {
    console.error('run process failed - main catch')
    console.error(e.message)
}
