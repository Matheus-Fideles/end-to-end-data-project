package org.data.master.infrastructure.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.data.master.application.domain.model.RespiratoryDiseases;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class CovidMovementDTO {

    @JsonProperty("mesAno")
    private String yearMonth;

    @JsonProperty("codigoFuncao")
    private String functionCode;

    @JsonProperty("funcao")
    private String function;

    @JsonProperty("codigoSubfuncao")
    private String subFunctionCode;

    @JsonProperty("subfuncao")
    private String subFunction;

    @JsonProperty("codigoPrograma")
    private String programCode;

    @JsonProperty("programa")
    private String program;

    @JsonProperty("codigoAcao")
    private String actionCode;

    @JsonProperty("acao")
    private String action;

    @JsonProperty("idPlanoOrcamentario")
    private Integer budgetPlanId;

    @JsonProperty("codigoPlanoOrcamentario")
    private String budgetPlanCode;

    @JsonProperty("planoOrcamentario")
    private String budgetPlan;

    @JsonProperty("codigoGrupoDespesa")
    private String expenseGroupCode;

    @JsonProperty("grupoDespesa")
    private String expenseGroup;

    @JsonProperty("codigoElementoDespesa")
    private String expenditureElementCode;

    @JsonProperty("elementoDespesa")
    private String expenditureElement;

    @JsonProperty("codigomodalidadedeDespesa")
    private String expenditureModeCode;

    @JsonProperty("modalidadeDespesa")
    private String expenditureMode;

    @JsonProperty("empenhado")
    private String pledged;

    @JsonProperty("pago")
    private String paid;

    @JsonProperty("liquidado")
    private String settled;

    public RespiratoryDiseases toDomain(){
        RespiratoryDiseases respiratoryDiseases = new RespiratoryDiseases();
        respiratoryDiseases.setYearMonth(yearMonth);
        respiratoryDiseases.setFunctionCode(functionCode);
        respiratoryDiseases.setFunction(function);
        respiratoryDiseases.setSubFunctionCode(subFunctionCode);
        respiratoryDiseases.setSubFunction(subFunction);
        respiratoryDiseases.setProgramCode(programCode);
        respiratoryDiseases.setProgram(program);
        respiratoryDiseases.setActionCode(actionCode);
        respiratoryDiseases.setAction(action);
        respiratoryDiseases.setBudgetPlanId(budgetPlanId);
        respiratoryDiseases.setBudgetPlanCode(budgetPlanCode);
        respiratoryDiseases.setBudgetPlan(budgetPlan);
        respiratoryDiseases.setExpenseGroupCode(expenseGroupCode);
        respiratoryDiseases.setExpenseGroup(expenseGroup);
        respiratoryDiseases.setExpenditureElementCode(expenditureElementCode);
        respiratoryDiseases.setExpenditureElement(expenditureElement);
        respiratoryDiseases.setExpenditureModeCode(expenditureModeCode);
        respiratoryDiseases.setExpenditureMode(expenditureMode);
        respiratoryDiseases.setPledged(pledged);
        respiratoryDiseases.setPaid(paid);
        respiratoryDiseases.setSettled(settled);

        return respiratoryDiseases;
    }

}
