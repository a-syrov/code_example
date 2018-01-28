from bashim.models import BashAbyssQuote, BashQuote
from rest_framework import serializers

class BashQuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BashQuote
        fields = (
        	'rating',
			'quote_id',
			'date',
			'text',
			'link',
			'comics',
			'comics_img_url',
			'comics_image',
			'is_comics',
        )


class BashAbyssQuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BashAbyssQuote
        fields = (
        	'quote_id',
			'date',
			'text',
        )