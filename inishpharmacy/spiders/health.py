# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import unicodedata


class HealthSpider(Spider):
    name = 'health'
    allowed_domains = ['inishpharmacy.com']
    start_urls = ['https://www.inishpharmacy.com/c/other-healthcare/299']

    def parse(self, response):
        items = response.xpath(
            '//div[@class="mz_product_info"]/h3/a/@href').extract()
        for item in items:
            absolute_url = response.urljoin(item)
            yield Request(absolute_url, callback=self.parse_page)

        # process next page
        next_page_url = response.xpath(
            '//a[text()="Next »"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_page(self, response):
        try:
            title = response.xpath(
                '//h1[@id="product-title"]/text()').extract_first()
        except:
            pass
        try:
            result = response.xpath(
                '//div[@class="breadcrumbContainer"]/ul/li//text()').extract()
            raw_category = "->".join(x for x in result).strip().replace(
                'Home->', '').replace('->Home', '')
            category = raw_category.replace('->' + title, '')
        except:
            pass

        try:
            price = response.xpath(
                '//span[@id="product-price"]/text()').extract_first().strip().replace('€', '')
        except:
            pass
        try:
            product_code = response.xpath(
                '//h5[@id="product-code"]/text()').extract_first().strip()
        except:
            pass
        try:
            raw_short_description = response.xpath(
                '//div[@id="product-short-description"]//text()').extract()
            short_description = " ".join(
                x.replace('\r\n', '').replace('•', '').replace('â€™', '’').replace('€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_short_description).strip()
        except:
            pass
        # try:
        #     raw_short_description = response.xpath(
        #         '//div[@id="product-short-description"]//p//text()').extract()
        #     short_description = " ".join(
        #         x.replace('\r\n', '').replace('•', '').replace('â€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_short_description).strip()
        # except:
        #     pass
        # try:
        #     raw_short_description_bullet = response.xpath(
        #         '//div[@id="product-short-description"]//ul//text()').extract()
        #     short_description_bullet = " ".join(
        #         x.replace('\r\n', '').replace('•', '').replace('â€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_short_description_bullet).strip().replace('\r\n->', '')
        # except:
        #     pass
        try:
            raw_long_description = response.xpath(
                '//div[@id="product-longdescription"]//text()').extract()
            long_description = " ".join(x.replace('\r\n', '').replace('•', '').replace('€™', '’').replace('â€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&')
                                        for x in raw_long_description).strip()
        except:
            pass
        try:
            raw_How_to_Use = response.xpath(
                '//dd[@id="product-short-description2"]//p//text()').extract()
            How_to_Use = " ".join(x.replace('\r\n', '').replace('•', '').replace('€™', '’').replace('â€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&')
                                  for x in raw_How_to_Use).strip()
        except:
            pass
        try:
            raw_Active_Ingredients = response.xpath(
                '//dd[@id="product-short-description3"]//p//text()').extract()
            Active_Ingredients = " ".join(
                x.replace('\r\n', '').replace('•', '').replace('€™', '’').replace('â€™', '’').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_Active_Ingredients).strip()
        except:
            pass

        # yield {
        #     'Title': unicodedata.normalize("NFC", title),
        #     'Category': unicodedata.normalize("NFC", category),
        #     'Price': unicodedata.normalize("NFC", price),
        #     'Product Code/ SKU': unicodedata.normalize("NFC", product_code),
        #     'Short Description': unicodedata.normalize("NFC", short_description),
        #     'Short Description Bullet': unicodedata.normalize("NFC",
        #                                                       short_description_bullet),
        #     'Long Description': unicodedata.normalize("NFC", long_description),
        #     'How to Use': unicodedata.normalize("NFC", How_to_Use),
        #     'Active Ingredients': unicodedata.normalize("NFC", Active_Ingredients),
        #     'Product URL': response.url,
        # }

        yield {
            'Title': title,
            'Category': category,
            'Price': price,
            'Product Code/ SKU': product_code,
            'Short Description': short_description,
            # 'Short Description Bullet': short_description_bullet,
            'Long Description': long_description,
            'How to Use': How_to_Use,
            'Active Ingredients': Active_Ingredients,
            'Product URL': response.url,
        }


# # -*- coding: utf-8 -*-
# from scrapy import Spider
# from scrapy.http import Request
# import unicodedata


# class HealthSpider(Spider):
#     name = 'health'
#     allowed_domains = ['inishpharmacy.com']
#     start_urls = ['https://www.inishpharmacy.com/c/embarassing-conditions/22']

#     def parse(self, response):
#         items = response.xpath(
#             '//div[@class="mz_product_info"]/h3/a/@href').extract()
#         for item in items:
#             absolute_url = response.urljoin(item)
#             yield Request(absolute_url, callback=self.parse_page)

#         # process next page
#         next_page_url = response.xpath(
#             '//a[text()="Next »"]/@href').extract_first()
#         absolute_next_page_url = response.urljoin(next_page_url)
#         yield Request(absolute_next_page_url)

#     def parse_page(self, response):
#         try:
#             title = response.xpath(
#                 '//h1[@id="product-title"]/text()').extract_first()
#         except:
#             pass
#         try:
#             result = response.xpath(
#                 '//div[@class="breadcrumbContainer"]/ul/li//text()').extract()
#             raw_category = "->".join(x for x in result).strip().replace(
#                 'Home->', '').replace('->Home', '')
#             category = raw_category.replace('->' + title, '')
#         except:
#             pass

#         try:
#             price = response.xpath(
#                 '//span[@id="product-price"]/text()').extract_first().strip().replace('€', '')
#         except:
#             pass
#         try:
#             product_code = response.xpath(
#                 '//h5[@id="product-code"]/text()').extract_first().strip()
#         except:
#             pass
#         try:
#             raw_short_description = response.xpath(
#                 '//div[@id="product-short-description"]//p//text()').extract()
#             short_description = " ".join(
#                 x.replace('\r\n', '').replace('•', '').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_short_description).strip()
#         except:
#             pass
#         try:
#             raw_short_description_bullet = response.xpath(
#                 '//div[@id="product-short-description"]//ul//text()').extract()
#             short_description_bullet = "->".join(
#                 x.replace('\r\n', '').replace('•', '').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_short_description_bullet).strip().replace('\r\n->', '')
#         except:
#             pass
#         try:
#             raw_long_description = response.xpath(
#                 '//div[@id="product-longdescription"]//text()').extract()
#             long_description = " ".join(x.replace('\r\n', '').replace('•', '').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&')
#                                         for x in raw_long_description).strip()
#         except:
#             pass
#         try:
#             raw_How_to_Use = response.xpath(
#                 '//dd[@id="product-short-description2"]//p//text()').extract()
#             How_to_Use = " ".join(x.replace('\r\n', '').replace('•', '').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&')
#                                   for x in raw_How_to_Use).strip()
#         except:
#             pass
#         try:
#             raw_Active_Ingredients = response.xpath(
#                 '//dd[@id="product-short-description3"]//p//text()').extract()
#             Active_Ingredients = " ".join(
#                 x.replace('\r\n', '').replace('•', '').replace('&nbsp;', '').replace('&rsquo;', '’').replace('&amp;', '&') for x in raw_Active_Ingredients).strip()
#         except:
#             pass

#         yield {
#             'Title': unicodedata.normalize("NFKD", title),
#             'Category': unicodedata.normalize("NFKD", category),
#             'Price': unicodedata.normalize("NFKD", price),
#             'Product Code/ SKU': unicodedata.normalize("NFKD", product_code),
#             'Short Description': unicodedata.normalize("NFKD", short_description),
#             'Short Description Bullet': unicodedata.normalize("NFKD",
#                                                               short_description_bullet),
#             'Long Description': unicodedata.normalize("NFKD", long_description),
#             'How to Use': unicodedata.normalize("NFKD", How_to_Use),
#             'Active Ingredients': unicodedata.normalize("NFKD", Active_Ingredients),
#             'Product URL': response.url,
#         }

#         # yield {
#         #     'Title': title.encode('utf-8'),
#         #     'Category': category.encode('utf-8'),
#         #     'Price': price.encode('utf-8'),
#         #     'Product Code/ SKU': product_code.encode('utf-8'),
#         #     'Short Description': short_description.encode('utf-8'),
#         #     'Short Description Bullet': short_description_bullet.encode('utf-8'),
#         #     'Long Description': long_description.encode('utf-8'),
#         #     'How to Use': How_to_Use.encode('utf-8'),
#         #     'Active Ingredients': Active_Ingredients.encode('utf-8'),
#         #     'Product URL': response.url,
#         # }
