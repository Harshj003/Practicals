.MODEL SMALL

.STACK 100H



.DATA

N DB 34H,67H,89H,12H,55H,90H,0CH

COUNT DW 7

LARGEST DB ?



.CODE

START:

MOV AX,@DATA

MOV DS,AX

MOV SI, 0 




MOV CX,COUNT

MOV BL,N[SI]

DEC CX

AGAIN:

INC SI

CMP BL,N[SI]

JNC NOSWAP

MOV BL,N[SI]

NOSWAP:LOOP AGAIN

MOV LARGEST,BL

MOV AH,4CH

INT 21H

END START
