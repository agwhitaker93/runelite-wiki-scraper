const fs = require('fs')

fs.readFile('resources/generated/Items.cache.json', (err, res) => {
    if (err) throw err

    console.log(JSON.parse(res)["Coal"])
})
