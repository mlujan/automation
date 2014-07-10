from sst.actions import *

go_to("http://www.biotrust.com")
assert_element(css_class="ShopCartButtonLink")
