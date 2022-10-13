select left(product_code,2) as 'CATEGORY', count(product_code)
from product
group by CATEGORY