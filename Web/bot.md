
# Stock Bot

1: Connected to <https://st0ck-b0t.vishwactf.com/>
2: Notice when a call to bot is made, it makes a request to '/Products/check.php'
3: To check for LFI I tried requesting check.php with curl and got a positive response:

```php
<?php

    if(isset(['product'])){
         = ['product'];
        header('Content-type: application\/json');
        if(strpos(,'Flag')){
             = array('Flag' => file_get_contents());
        }
        else{
             = array('Quantity' => file_get_contents());
        }
        echo json_encode();
    }

?>
```

4: Also made a request to '../index.php', got a hint: `"Hint: Along with other products the Flag is also available in the Products directory"`
5: Requested Flag with curl and got it, it's probably not shown in the main website because the bots doesn't give it to us

**VishwaCTF{b0T_kn0w5_7h3_s3cr3t}**
