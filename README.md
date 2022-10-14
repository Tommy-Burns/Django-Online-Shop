# Django Online Shop
 An Ecommerce Application built with Django (Fly Buy)


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