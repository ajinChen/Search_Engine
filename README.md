# Search_Engine
Search Engine Design<br>
Sep 2021

Project description<br>
• Visualize search results in a browser window, which is able to highlight search terms and navigate to documents using HTML.<br>
• Implement hashtable and index table using Python to significantly improve search speed in the large data set search engine.<br>
• Design a pipeline for convert different file contexts (.csv / .xml / .json / .html).<br>


<b><u>Linear Search</u></b><br>
Linear search just like we put all items in one bucket and find them one by one in this container. In the ‘create_linear_table’ function, we create an unordered list of tuples containing all cities and their corresponding populations appending all elements in a list structure. 

![Screen Shot1](https://user-images.githubusercontent.com/86497342/136708014-e34423a9-197d-4f27-81fc-6f58d0271410.png)




<b><u>htable_get()</u></b><br>
The htable_get function is our lookup function that takes in 2 parameters: the hash table created and the key of interest. The function first utilizes the hashcode function to get the index of the bucket where the key is located. It then searches linearly within that specific bucket to look for the key. If the key is found, the function will return its value, otherwise it will return None. 

For this particular example, you can see that using a hash table speeds up the time it takes to look up Yucca Valley’s population by about 4 times. 

![Screen Shot 2021-10-10 at 10 57 40 AM](https://user-images.githubusercontent.com/86497342/136708014-e34423a9-197d-4f27-81fc-6f58d0271410.png)
