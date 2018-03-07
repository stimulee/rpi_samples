# Servomoteur et API
Ici plusieurs notions intéressantes :
- créer une api http basic pour lancer des scripts python grâce à une simple URL
- manipuler un servomoteur

## serveur API :
Lancer le serveur HTTP qui expose les scripts :

```shell
   chmod +x ./start.py
   chmod u+x ./script/*
   ./start.py
```

## Servomoteur usage :
* Manuellement :
```shell
   python script/servo.py -souverture
   python script/servo.py -sfermeture
```

* Via API :
```
   http://localhost:8080/servo.py?s=fermeture
```

sources :
* http://demonter.net/2013/11/02/comment-piloter-un-servomoteur-a-laide-dun-raspberry-et-du-port-gpio/
* https://github.com/bewiwi/py-script
