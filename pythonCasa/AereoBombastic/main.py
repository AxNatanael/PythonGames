import time 
import pygame
import random 

pygame.font.init()

LARGHEZZA, ALTEZZA = 1000, 700
FINESTRA = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Aero Bombastic")

BG = pygame.transform.scale(pygame.image.load("AereoBombastic/images/beckgrounSpaceIa.png"), (LARGHEZZA, ALTEZZA))  # trasform.scale serve per adattare l' immagine alla finestra

PLAYER_LARGEZZA = 40
PLAYER_ALTEZZA = 60
PLAYER_VEL = 5

LARGHEZZA_PROIETTILE = 10
ALTEZZA_PROIETTILE = 20

FONT = pygame.font.SysFont("comic sans ms", 30)

def draw(player, tempo_gioco):
    FINESTRA.blit(BG, (0, 0))   # blit è una funzione che serve per settare lo sfondo in una finestra  la coordinata 0,0 angolo alto sinistro
    testo_font = FONT.render(f"Tempo gioco: {round(tempo_gioco)}s", 1 ,"white") #la f davanti si usa per fare stringa con variabile
    FINESTRA.blit(testo_font, (10,10))
    pygame.draw.rect(FINESTRA, (255, 0, 0), player) # dove vogliamo disegnare un rettangolo , colore , coordinate
    pygame.display.update()

def main(): 
    run = True  
    player = pygame.Rect(400, ALTEZZA - PLAYER_ALTEZZA, PLAYER_LARGEZZA, PLAYER_ALTEZZA)    #passiamo alla variabile player la posizione e le sue dimensioni
    clock = pygame.time.Clock()   #creo una variabile che mi gestisca i frame per secondo , altrimenti va in base alla velocità del computer
    start_time = time.time()    #la variabile che sa quando parte il gioco 
    incremento_proiettili = 2000
    contatore_proiettili = 0

    proiettili = []

    while run:  #creo un ciclo while per tenere la schermata attiva
        contatore_proiettili += clock.tick(60)  #decido il numero massimo di frame per secondo 
        tempo_gioco = time.time() - start_time  #teniamo conto dei seondo che passa nel gioco da quando e partito  
        
        if contatore_proiettili > incremento_proiettili:
            for _ in range(3):
                proiettile_x = random.randint(0, LARGHEZZA - LARGHEZZA_PROIETTILE)
                proiettile = pygame.Rect(proiettile_x, -ALTEZZA_PROIETTILE, LARGHEZZA_PROIETTILE, ALTEZZA_PROIETTILE)
                proiettili.append(proiettile)
            
            incremento_proiettili = max(200, incremento_proiettili - 50)
            contatore_proiettili = 0

        for event in pygame.event.get():    #faccio un controllo in modo da chiudere la schermata quando premo la x
            if event.type == pygame.QUIT:   #immagino che pygame.QUIT intenda la x della scheda
                run = False
                break
        
        tasti = pygame.key.get_pressed()  #crea una lista di tutti i tasti premuti dall utente e ci dice se sono premuti o no 
        if tasti[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:  #controllo per non uscire dai bordi
            player.x -= PLAYER_VEL
        if tasti[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= LARGHEZZA:   # controllo per non uscire dal bordo di destra 
            player.x += PLAYER_VEL
       
        draw(player, tempo_gioco)
    
    pygame.quit()

if __name__ == "__main__":
    main()    