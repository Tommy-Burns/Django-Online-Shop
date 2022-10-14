# Django Online Shop
 An Ecommerce Application built with Django **(Fly Buy)**


 The packages used are found in the ```requirements.txt``` file.

## The app has the following functionalities
- Group products by categories
- A shopping cart using Django sessions
- Create custom context processors
- Managing customer orders
- Asynchronous notifications using [Celery](https://docs.celeryq.dev/) and [RabbitMQ](https://www.rabbitmq.com/)
- Integrate [Stripe](https://stripe.com/) to process payments
- A webhook to receive payment notifications from Stripe
- Custom admin actions to generate CSV and PDF files from invoices
- A coupon system to apply disconts to orders
- Integrate discounts with Stripe payments
- A product recommendation engine using Redis
- Internationalization (User can translate between English and Spanish)
---
# Below are some screenshots
### Homepage in English
![Homepage in English](./README%20Images/1-all-en.jpg)
### Homepage in Spanish
![Homepage in Spanish](./README%20Images/2-all-es.jpg)
### Category Page in English
![Category Page in English](./README%20Images/3-local-en.jpg)
### Category page in Spanish
![Category page in Spanish](./README%20Images/4-local-es.jpg)
### Another category page in Spanish
![Category page in Spanish 2](./README%20Images/6-elec-es.jpg)
### Product detail page in English
![Product detail page in English](./README%20Images/7-detail-en.jpg)
### Product detail page in Spanish
![Product detail page in Spanish](./README%20Images/8-detail-es.jpg)
### Cart page with applied coupon
![Cart page](./README%20Images/9-cart-en.jpg)
### Checkout page
![Checkout page](./README%20Images/10-checkout-en.jpg)
### Order summary page
![Order page](./README%20Images/11-order-summary.jpg)
### Stripe card details page
***Details provided are test mode details and are not valid for any real payment***

![Card details](./README%20Images/12-card-details.jpg)
### Stripe card processing page
![Card procesing](./README%20Images/13-processing.jpg)
### Stripe card success page
![Card success](./README%20Images/14-success.jpg)
### Successful payment page
![Success page](./README%20Images/15-done.jpg)

---

```python
print('🎉🎉🎉🎉🎉🎉')
while True:
    if os.path.isfile('manage.py'):
        shell.run(
            "python manage.py runserver"
        )
```
## Author

LinkedIn - [Thomas Burns Botchwey](www.linkedin.com/in/tbbotchwey)

## Credit

[Antonio Melé](https://antoniomele.es/)  
[Django 4 by Example](https://djangobyexample.com/)