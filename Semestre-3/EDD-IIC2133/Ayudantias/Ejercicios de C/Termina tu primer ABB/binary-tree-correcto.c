#include <stdio.h>    // para printf y scanf (operaciones input/output)
#include <stdlib.h>   // para malloc
#include <stdbool.h>

// Código base correcto.

//////////////////////////////////////////////////////
////// PROBLEMA ABB (ÁRBOL BINARIO DE BÚSQUEDA) //////
//////////////////////////////////////////////////////
//// Momento en que les será más útil: previo T1! ////
//////////////////////////////////////////////////////

/* DISCLAIMER
 Este código NO está modularizado.
 para las tareas JAMÁS se espera esto. Notar que 
 se incurre en la mala práctica anterior meramente
 para brindar simplicidad al ejemplo.
*/ 

/* CÓMO CORRER
 gcc binary-tree.c [-g] -o binary-tree
 con valgrind: valgrind --leak-check=full ./binary-tree
 sin valgrind: ./binary-tree
*/


typedef struct TreeNode {
    // usar typedef permite llamar desde fuera al 
    // struct como "treeNode" en vez de "struct TreeNode"
    int nodeID;
    int value;
    struct TreeNode * left;
    struct TreeNode * right;
} treeNode; 


struct TreeNode * createNode(int nodeID, int value) {
    treeNode * newNode = calloc(1, sizeof(treeNode));

    // Como treeNode es un puntero acedemos a sus elementos con "->"
    newNode->nodeID = nodeID; 
    newNode->value = value;
    newNode->left = NULL; // null == false
    newNode->right = NULL;

    return newNode;
}


void insertNode(treeNode * rootNode, treeNode * nodeToInsert) {

    treeNode * pCurrentNode = rootNode;
    bool isInserted = false;

    while (!isInserted) {
        if (pCurrentNode->value > nodeToInsert->value) {
            // candidato a hijo izquierdo.
            if (pCurrentNode->left) {
                pCurrentNode = pCurrentNode->left;
            } else {
                pCurrentNode->left = nodeToInsert;
                isInserted = true;
            }
        } else { // notar que si hay empate en value, se va al lado derecho.
            if (pCurrentNode->right) {
                pCurrentNode = pCurrentNode->right;
            } else { 
                pCurrentNode->right = nodeToInsert; 
                isInserted = true;
            }
        }
    }
}


void printTree(treeNode * rootNode) {
    /*  NO TOCAR. Pero si leer comentario abajo  */

    treeNode * pCurrentNode = rootNode;

    printf("         (%i)  \n", pCurrentNode->value);
    printf("   (%i)        (%i)  \n", pCurrentNode->left->value, pCurrentNode->right->value);
    printf("(%i)   (%i) (%i)   (xx)   \n", pCurrentNode->left->left->value, pCurrentNode->left->right->value, pCurrentNode->right->left->value);
    printf("             (%i)    \n",  pCurrentNode->right->left->right->value);
    // (xx) -> No es un nodo, solo se muestra para favorecer la visualización de un árbol en el print.


}


void freeTree(treeNode * rootNode) {
    /*  NO TOCAR  */

    treeNode * pCurrentNode = rootNode;

    if (pCurrentNode->left) { freeTree(pCurrentNode->left); }
    if (pCurrentNode->right) { freeTree(pCurrentNode->right); }

    free(pCurrentNode);
}


int main() {

    // Se crea el árbol el cual tendra 7 nodos en total.
    int values[] = {20, 15, 32, 7, 18, 23, 28};
    treeNode * rootNode = createNode(0, values[0]);
    
    // Es importante que se respete el órden de inserción 
    // según values para que lleguemos al mismo árbol.
    for (int i = 1; i < 7; i++) { 
        treeNode * nodeToInsert = createNode(i, values[i]);
        insertNode(rootNode, nodeToInsert);
    }

    printTree(rootNode);

    // LIBERAR MEMORIA !! monkey
    freeTree(rootNode);

    return 0; // buena práctica.
}
