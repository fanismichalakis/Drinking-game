# Drinking-game

Ce jeu a été réalisé dans le cadre de l'autonomie d'informatique en deuxième année à l'Ecole Centrale de Marseille.

L'ambition était de créer un jeu à boire composé de deux mini-jeux : un quizz et un jeu d'adresse. Le joueur est invité à choisir au début de son tour entre le jeu d'adresse et le quizz. En fonction de sa réussite, il doit ensuite distribuer des gorgées à ses partenaires de jeu, ou boire lui-même lesdites gorgées.

L'ensemble des fonctionnalités n'a pas pu être réalisé, puisque le temps imparti n'était que de quelques heures d'autonomie. Cependant, nous sommes parvenus à réaliser un prototype fonctionnel.

Ce qui a été fait :
--

- le quizz fonctionne correctement. Il comporte 8 questions, mais il est simple d'en ajouter de nouvelles. Le joueur clique sur la réponse qu'il pense être la bonne, s'il a juste il est invité à distribuer 2 gorgées, s'il a faux il est invité à en boire 2. Il peut ensuite cliquer sur "Continuer" pour répondre à une nouvelle question.

- le jeu d'adresse consiste à déplacer une boule blanche tout en évitant les boules rouges arrivant depuis la droite selon des angles pseudo-aléatoires. La vitesse des boules rouges augmente avec le temps, le but étant de tenir le plus longtemps possible. Lorsque le joueur percute une boule rouge, une pop-up l'en informe et lui indique le nombre de gorgées qu'il doit boire.
  
Ce qu'il reste à faire :
--

- permettre de retourner au menu de sélection du mini-jeu sans avoir à fermer l'application et la rouvrir

- instaurer un seuil de temps pour le jeu d'adresse, au bout duquel le joueur est considéré comme victorieux et peu distribuer des gorgées

- faire en sorte que le jeu d'adresse s'arrête une fois que le joueur a percuté une boule rouge

- faire en sorte qu'une question déjà posée dans le quizz ne puisse plus être posée de nouveau au cours de cette partie

- pour les parties à plus de deux joueurs, tenir une liste des noms de joueurs pour pouvoir désigner celui dont c'est le tour, éventuellement indiquer des actions du type "Alice distribue 2 gorgées à Bob" en cas de victoire d'Alice, ou encore tenir un compte des scores pour désigner un vainqueur à la fin du jeu.
  
En espérant que ce jeu vous plaira,

Emmanuel KRIEGER et Fanis MICHALAKIS

PS: Il y a un fichier .kv et la consigne était de ne pas en avoir, nous en avons conscience, sauf que nous n'avons pas réussi à utliser la commande self.canvas.add() pour tous les widgets. Avec plus de temps, cela aurait été très sûrement faisable mais nous avons préféré vous envoyer quelque chose qui marchait.
