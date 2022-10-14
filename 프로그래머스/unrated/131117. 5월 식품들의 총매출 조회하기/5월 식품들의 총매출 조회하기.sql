select fp.product_id, fp.product_name, sum(fo.amount) * fp.price as 'total'
from food_product as fp
join food_order as fo
on fp.product_id = fo.product_id
where year(fo.produce_date) = 2022 and month(fo.produce_date) = 5
group by fp.product_id
order by total desc, fp.product_id