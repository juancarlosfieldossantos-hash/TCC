from flask import blueprint,request
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import aluno

aluno_service = AlunoService()

alluno controller = Blueprint('aluno', __name__, url_perfix='/alunos')

@aluno_controller.route('/', methods=['GET'])
def listar_alunos():
    alunos = aluno_Service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route('/', methods= ['POST'])
def adicionar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=0, dados["nome"])
                      idade=dados["idade"], cpf=dados["cpf"]    
    aluno_service.adicionar_aluno(obj_aluno)
    return jsonify(aluno)

@aluno_controler.route('/<int:id>', methods['GET'])
def obter_aluno(id):
        aluno = AlunoService.obter_aluno_por_id(id)
        if aluno:
           returnjsonify(aluno)
        else:
                return jsonify({"erro": "aluno não encontrado"}),404
        
@aluno_controller_route('/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    sucesso = aluno_service.remover_aluno(id)
    return jsonify(sucesso)

@aluno_controller.route('/',methods=['PUT'])
def atualizar_aluno():
        dados = request.get_json()
        obj_aluno = aluno(id=dados["id"],nome = dados["nome"],
                          idade = dados[dados"idade"], cpf=dados["cpf"])
        aluno = alino_service.atualizar_aluno(obj_aluno)
        if aluno:
               return jsonify(aluno)
        else:
               return jsonify({"erro": "aluno não encontrado"}),404