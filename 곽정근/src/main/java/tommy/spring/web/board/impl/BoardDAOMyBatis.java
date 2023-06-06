package tommy.spring.web.board.impl;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import tommy.spring.web.board.BoardVO;

@Repository
public class BoardDAOMyBatis {
	@Autowired
	private SqlSessionTemplate sqlSessionTemplate;

	public void insertBoard(BoardVO vo) {
		System.out.println("---> MyBatis�� insertBoard() ��� ó��");
		sqlSessionTemplate.insert("BoardDAO.insertBoard", vo);
	}

	public void updateBoard(BoardVO vo) {
		System.out.println("---> MyBatis�� updateBoard() ��� ó��");
		sqlSessionTemplate.update("BoardDAO.updateBoard", vo);
	}

	public void deleteBoard(BoardVO vo) {
		System.out.println("---> MyBatis�� deleteBoard() ��� ó��");
		sqlSessionTemplate.delete("BoardDAO.deleteBoard", vo);
	}

	public BoardVO getBoard(BoardVO vo) {
		System.out.println("---> MyBatis�� getBoard() ��� ó��");
		return (BoardVO) sqlSessionTemplate.selectOne("BoardDAO.getBoard", vo);
	}

	public List<BoardVO> getBoardList(BoardVO vo) {
		System.out.println("---> MyBatis�� getBoardList() ��� ó��");
		return sqlSessionTemplate.selectList("BoardDAO.getBoardList", vo);
	}
}
