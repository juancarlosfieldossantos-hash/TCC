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
    aluno_service.adicionar_aluno(obj_aluno)