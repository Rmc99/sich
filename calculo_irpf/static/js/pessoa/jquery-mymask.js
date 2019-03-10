$(document).ready(function () {
        var $id_cpf = $("#id_cpf");
        $id_cpf.mask('000.000.000-00', {reverse: true});

        var $id_telefone = $("#id_telefone");
        $id_telefone.mask('00-00000-0000', {reverse: true});
    }
);


