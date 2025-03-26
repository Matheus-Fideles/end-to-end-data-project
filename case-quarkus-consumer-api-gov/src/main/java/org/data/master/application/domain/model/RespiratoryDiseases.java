package org.data.master.application.domain.model;

import java.util.List;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Getter;
import lombok.Setter;


@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class RespiratoryDiseases extends PanacheEntity {

    private String yearMonth;
    private String functionCode;
    private String function;
    private String subFunctionCode;
    private String subFunction;
    private String programCode;
    private String program;
    private String actionCode;
    private String action;
    private Integer budgetPlanId;
    private String budgetPlanCode;
    private String budgetPlan;
    private String expenseGroupCode;
    private String expenseGroup;
    private String expenditureElementCode;
    private String expenditureElement;
    private String expenditureModeCode;
    private String expenditureMode;
    private String pledged;
    private String paid;
    private String settled;
    private Integer months;
    private Integer years;

    public static List<RespiratoryDiseases> findRespiratoryDiseasesByYearAndMonth(
        Integer year,
        Integer month,
        Integer page,
        Integer size
    ) {
        return find(
            "years = ?1 and months= ?2 ", 
            year, 
            month
        ).page(page, size)
        .list();
    }
    
    public static List<RespiratoryDiseases> findRespiratoryDiseasesByYear(
        Integer year,
        Integer page,
        Integer size
    ) {
        return find(
            "years = ?1", 
            year
        ).page(page, size)
        .list();
    }

    public static List<RespiratoryDiseases> findRespiratoryDiseasesByMonth(
        Integer month,
        Integer page,
        Integer size
    ) {
        return find(
            "months = ?1", 
            month
        ).page(page, size)
        .list();
    }

    public static List<RespiratoryDiseases> findAllRespiratoryDiseases(
        Integer page,
        Integer size
    ) {
        return findAll().page(page, size).list();
    }
    
}
