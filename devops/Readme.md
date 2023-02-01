# Test technique - DevOPS
### Contexte
Vous venez de rejoindre SensCritique et on vous demande de reprendre le projet "Tartuffe".
Le projet Tartuffe, c'est une API qui permet de récupérer les notes des livres SensCritique.
**Problème :** Le projet a été maintenu par un devOPS d'une ESN et c'est l'enfer ! Rien ne fonctionne !
Vous allez donc nous aider à corriger toutes les inepties du devOPS.

### Installation
* `docker-compose up` pour lancer le projet
* `curl localhost/book/<id>` pour récupérer un livre
* `curl localhost/books` pour récupérer tous les livres

### Missions
*Note : Merci d'expliquer vos choix et/ou investigation pour chaque "missions"* 
- [ ] Debugger le projet et faites en sorte que l'API réponde sur la route `GET /books`
- [ ] Réorganiser le projet comme bon vous semble, profitez-en pour corriger les incohérences.
- [ ] Intégrer un système de cache au projet (Redis par exemple)
      Note: Quand on cherche à récupérer un livre, on doit vérifier l'existence dans le cache avant de regarder dans le fichier books.json
      Note2: Le fichier books.json fait office de "base de données" pour simplifier le test technique, vous n'êtes pas obligé d'y toucher.
- [ ] Faites en sorte que la page de statistiques d'HaProxy fonctionne
- [ ] L'api Denver (service api_denver dans le docker-compose.yaml) ne répond pas à 100% du temps, au bout d'un moment elle arrête de répondre, pourtant elle ne fait pas grand chose: elle affiche juste un livre aléatoire. Pourquoi bug t-elle ? trouvez la solution
