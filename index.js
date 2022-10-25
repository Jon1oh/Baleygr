const port = 8000
const axios = require('axios')
const cheerio = require('cheerio')
const { response } = require('express')
const express = require('express')

const app = express()
const url = 'https://www.theguardian.com/uk'
axios(url).then(response => {
    const html = response.data
    const get_html = cheerio.load(html)
    const articles = []

    get_html('.fc-item__title', html).each(function() {
        const title = get_html(this).text()
        const url = get_html(this).find('a').attr('href')
        articles.push({
            title,
            url
        })
    })
    console.log(articles)
}).catch(error => console.log(error))

app.listen(port, () => console.log('server running on PORT' + ' ' + port))