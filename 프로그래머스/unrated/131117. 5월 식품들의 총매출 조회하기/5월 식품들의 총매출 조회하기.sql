select p.product_id, p.product_name, p.price*sum(o.amount) as total_sales
from food_order as o
join food_product as p
on o.product_id = p.product_id
where year(produce_date)=2022 and month(produce_date)=5
group by p.product_id
order by total_sales desc, p.product_id asc;