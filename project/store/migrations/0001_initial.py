# Generated by Django 4.1.7 on 2023-03-22 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('e_name', models.CharField(max_length=50)),
                ('effective_material', models.CharField(default='المادة الفعالة', max_length=100)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('usage', models.TextField(default='الاستخدام', max_length=200)),
                ('description', models.TextField(default='الوصف', max_length=300)),
                ('public_price', models.FloatField(default=100.0)),
                ('letter', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=20)),
                ('shape', models.CharField(choices=[('افلام', 'افلام'), ('اقراص', 'اقراص'), ('اكياس', 'اكياس'), ('امبولات', 'امبولات'), ('اسبراي', 'اسبراي'), ('اسبراي الانف', 'اسبراي الانف'), ('اسبراي الفم', 'اسبراي الفم'), ('اقراص استحلاب', 'اقراص استحلاب'), ('اقماع شرجية', 'اقماع شرجية'), ('اقماع مهبلية', 'اقماع مهبلية'), ('المحلول', 'المحلول'), ('برطمان', 'برطمان'), ('بلسم', 'بلسم'), ('بودرة', 'بودرة'), ('بودرة استنشاق', 'بودرة استنشاق'), ('جل', 'جل'), ('جل للعين', 'جل للعين'), ('جل مهبلي', 'جل مهبلي'), ('حبيبات فوارة', 'حبيبات فوارة'), ('حقنة معباة', 'حقنة معباه'), ('حليب مجفف', 'حليب مجفف'), ('خرطوشة', 'خرطوشة'), ('رغوة', 'رغوة'), ('زيت', 'زيت'), ('سائل', 'سائل'), ('شامبو', 'شامبو'), ('شراب', 'شراب'), ('صابون', 'صابون'), ('غسول للفم', 'غسول للفم'), ('غسول مهبلي', 'غسول مهبلي'), ('فيال', 'فيال'), ('قطرة انف', 'قطرة انف'), ('قطرة الاذن', 'قطرة الاذن'), ('قطرة للعين', 'قطرة للعين'), ('قطعة', 'قطعة'), ('قلم معبأ', 'قلم معبأ'), ('كبسولات', 'كبسولات'), ('كريم', 'كريم'), ('كريم مهبلي', 'كريم مهبلي'), ('لاصقات', 'لاصقات'), ('لوشن', 'لوشن'), ('لولب', 'لولب'), ('محلول استنشاق', 'محلول استنشاق'), ('محلول شرجي', 'محلول شرجي'), ('محلول وريدي', 'محلول وريدي'), ('مرهم', 'مرهم'), ('مرهم شرجي', 'مرهم شرجي'), ('مرهم للعين', 'مرهم للعين'), ('مستحلب', 'مستحلب'), ('معجون اسنان', 'معجون اسنان'), ('معلق', 'معلق'), ('نقط فم', 'نقط فم')], max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.company')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('price', models.FloatField(default=100.0)),
                ('offer_details', models.CharField(default='تفاصيل العرض', max_length=100)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='account.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_received', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='store.cart')),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_of_stock', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='store.item')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='account.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderoffers', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDiscounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdiscounts', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.discount')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.section'),
        ),
        migrations.AddField(
            model_name='discount',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='store.item'),
        ),
        migrations.AddField(
            model_name='discount',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='account.pharmacy'),
        ),
        migrations.CreateModel(
            name='CartOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='offers', to='store.cart')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardoffers', to='store.offer')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carditems', to='store.stock')),
            ],
        ),
        migrations.CreateModel(
            name='CartDiscounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='discount', to='store.cart')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carddiscount', to='store.discount')),
            ],
        ),
    ]
