from rolepermissions.roles import AbstractUserRoles

class user_voluntarios(AbstractUserRoles):
    available : {'ver_projetos' : True , 'editar_suas_infos': True , 'voluntariar' : True , 'candidatar_embaixador' : True,
                'fazer_doacao' : True, 'visualizar_atualizacoes_proj' : True, 'visualizar_info_contato_proj' : True, 
                'filtrar_localidade' : True, 'visualizar_embaixadores' : True, 'filtrar_localidade_embaixador' : True, 
                'ver_relatorios_semestrais' : True, 'cadastrar' : True, 'visualizar_infos_embaixadores' : True}

class embaixador(AbstractUserRoles) :
    available : {'pedidos_projetos' : True , 'filtro_localidade' : True , 'visualizar_embaxadores_resp' : True ,
                'sinalizar_respons' : True , 'ver_projetos' : True, 'divulgar_minha_pagina' : True , 'add_dados_perfil' : True}
    
class donoDeProjeto(AbstractUserRoles) :
    available : {'cadastrar_projetos' : True, 'visualizar_dados_voluntarios' : True, 'aprovar_voluntarios' : True, 'indicar_doacoes' : True, 
                'indicar_mais_voluntarios' : True, 'atualizar_dados_cadastrais' : True, 'adicionar_info_contato' : True,
                'atualizar_dados_meu_projeto' : True, 'enviar_relatorios_semestrais' : True, 'receber_not_doacoes' : True}

class gerenteDeProjeto(AbstractUserRoles) :
    available : {'inserir_relatorios' : True , 'Armazenar_dados_projetos' : True, 'permitir_voluntario' : True, 
                   'visualizar_voluntarios' : True, 'visualizar_embaixadores' : True ,'visualizar_relatorio' : True, 
                   'visualiar_projetos' : True , 'permitir_embaixador' : True, 'permitir_projeto' : True, 'visualizar_doacoes' : True}

