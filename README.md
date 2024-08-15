A fun path optimation program i developed in python using djikstra's algrithm.
 the use case is for a pokemon draft league I do with my college friends. We are given a map with towns/cities and routes connecting them (identical to the overworld map in the Pokemon games). 
 Each named route and city/town has a small pool of pokemon to draft from. There are only one of each pokemon to claim so there is a race element to the draft. 
 As a fun way to help expedite counting paths and find the most optimal pathways I came up with this! 

 To implement a path finding solution I needed to translate each city/town and named route to a node, and each non-designated 'route' connection to an edge. 
 An extra wrinkle to the fun: there was an action to 'fly' from any location back to the starting village instead of a normal move. This only went one direction. 
 To solve this I made the graph directional with every adjacent town/city/route bidirectional and every node having a one directional adjacent edge back to the starting town. 

![image](https://github.com/user-attachments/assets/03df758b-9e0b-4c51-9a91-5b7c2a1fad91) - simplified map.
![image](https://github.com/user-attachments/assets/404edbd4-026d-4a9c-9a49-bca87416f414) - full map.

