graph TD
1([Start]) --> 2["a ← x<br/> b ← y<br/>c ← z<br/>"]
2 --> 3{a > b}
3 -->|Yes| 4{a > c}
4 -->|No| 8[/Output c/]
4 --> |Yes| 6[/Output a/]
3 -->|No| 5{b > c}
5 --> |No| 6
5 --> |Yes| 7[/Output b/]
7 --> 9([Stop])
6 --> 9
8 --> 9
